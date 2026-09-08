import importlib.util
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
CALCULATORS = [
    ROOT / "plugins/morningwealth/skills/valuation-deep-dive/scripts/valuation.py",
    ROOT / "plugins/morningwealth/skills/valuation-deep-dive-html-report/scripts/valuation.py",
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
