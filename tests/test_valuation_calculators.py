from contextlib import redirect_stdout
import importlib.util
import io
import pathlib
import subprocess
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
CALCULATORS = [
    ROOT / "plugins/encryptedarc/skills/valuation-deep-dive/scripts/valuation.py",
    ROOT / "plugins/encryptedarc/skills/valuation-deep-dive-html-report/scripts/valuation.py",
]


def load_calculator(path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(f"valuation_{path.parent.parent.name}", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def assert_value_error(test_case: unittest.TestCase, callback):
    try:
        callback()
    except ValueError:
        return
    except Exception as error:
        test_case.fail(f"expected ValueError, got {type(error).__name__}: {error}")
    test_case.fail("expected ValueError, but no exception was raised")


class ValuationCalculatorTests(unittest.TestCase):
    def test_zero_terminal_growth_preserves_constant_excess_returns(self):
        for path in CALCULATORS:
            with self.subTest(path=path):
                calculator = load_calculator(path)
                value, _, _, terminal = calculator.residual_income(
                    100.0, [0.15, 0.15], 0.10, terminal_g=0.0
                )
                self.assertAlmostEqual(value, 150.0)
                self.assertAlmostEqual(terminal, 41.32231404958677)

    def test_zero_terminal_growth_preserves_negative_excess_returns(self):
        for path in CALCULATORS:
            with self.subTest(path=path):
                calculator = load_calculator(path)
                value, _, _, _ = calculator.residual_income(
                    100.0, [0.05, 0.05], 0.10, terminal_g=0.0
                )
                self.assertAlmostEqual(value, 50.0)

    def test_omitted_terminal_growth_preserves_finite_forecast(self):
        for path in CALCULATORS:
            with self.subTest(path=path):
                calculator = load_calculator(path)
                value, _, _, terminal = calculator.residual_income(
                    100.0, [0.15, 0.15], 0.10
                )
                self.assertAlmostEqual(value, 108.67768595041322)
                self.assertEqual(terminal, 0.0)

    def test_terminal_growth_is_continuous_through_zero(self):
        for path in CALCULATORS:
            for growth, expected in [(-0.02, 142.42424242424244),
                                     (0.02, 161.36363636363637),
                                     (0.00000001, 150.00000454545497)]:
                with self.subTest(path=path, growth=growth):
                    calculator = load_calculator(path)
                    value, _, _, _ = calculator.residual_income(
                        100.0, [0.15, 0.15], 0.10, terminal_g=growth
                    )
                    self.assertAlmostEqual(value, expected)

    def test_terminal_growth_must_be_below_cost_of_equity_including_zero(self):
        for path in CALCULATORS:
            for cost_of_equity, growth in [(0.0, 0.0), (0.1, 0.1), (0.1, 0.11)]:
                with self.subTest(path=path, cost_of_equity=cost_of_equity, growth=growth):
                    calculator = load_calculator(path)
                    with self.assertRaises(ValueError):
                        calculator.residual_income(
                            100.0, [0.15], cost_of_equity, terminal_g=growth
                        )

    def test_dcf_cli_deducts_and_echoes_non_common_equity_claims(self):
        for path in CALCULATORS:
            with self.subTest(path=path):
                result = subprocess.run(
                    [sys.executable, "-B", "-X", "utf8", str(path), "dcf", "--flows", "100,100",
                     "--wacc", "0.1", "--terminal-g", "0", "--net-cash", "25",
                     "--shares", "10", "--minority", "75", "--preferred", "25"],
                    capture_output=True, text=True, encoding="utf-8",
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertRegex(result.stdout, r"value per share\s+:\s+92\.50\b")
                self.assertRegex(result.stdout, r"minority interest\s+:\s+75\.00\b")
                self.assertRegex(result.stdout, r"preferred\s+:\s+25\.00\b")

    def test_residual_income_cli_distinguishes_omitted_and_zero_growth(self):
        for path in CALCULATORS:
            for arguments, expected in [([], "108.68"), (["--terminal-g", "0"], "150.00")]:
                with self.subTest(path=path, arguments=arguments):
                    calculator = load_calculator(path)
                    output = io.StringIO()
                    with redirect_stdout(output):
                        exit_code = calculator.main(
                            ["residual-income", "--bvps", "100", "--roes", "0.15,0.15",
                             "--coe", "0.1", *arguments]
                        )
                    self.assertEqual(exit_code, 0)
                    self.assertRegex(output.getvalue(),
                                     r"= value per share\s+:\s+" + expected.replace(".", r"\.") + r"\b")

    def test_dcf_cli_preserves_calls_without_non_common_equity_claims(self):
        for path in CALCULATORS:
            with self.subTest(path=path):
                result = subprocess.run(
                    [sys.executable, "-B", "-X", "utf8", str(path), "dcf", "--flows", "100,100",
                     "--wacc", "0.1", "--terminal-g", "0", "--net-cash", "25",
                     "--shares", "10"],
                    capture_output=True, text=True, encoding="utf-8",
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertRegex(result.stdout, r"value per share\s+:\s+102\.50\b")

    def test_rejects_zero_exit_multiple(self):
        for path in CALCULATORS:
            with self.subTest(path=path):
                calculator = load_calculator(path)
                assert_value_error(
                    self,
                    lambda: calculator.scenario_price(100.0, 0.0, 0.0, 10.0),
                )

    def test_rejects_empty_through_cycle_margin_series(self):
        for path in CALCULATORS:
            with self.subTest(path=path):
                calculator = load_calculator(path)
                assert_value_error(
                    self,
                    lambda: calculator.normalized_eps(100.0, [], 10.0),
                )
