from html.parser import HTMLParser
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHAT_SKILL = ROOT / "plugins/encryptedarc/skills/valuation-deep-dive"
REPORT_SKILL = ROOT / "plugins/encryptedarc/skills/valuation-deep-dive-html-report"
REFERENCE_FILES = {
    "archetype-playbooks.md",
    "core-finance-principles.md",
    "data-sourcing-valuation.md",
    "dcf-and-cost-of-capital.md",
    "peer-calibration.md",
    "thai-market-notes.md",
}


class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = []
        self._in_heading = False

    def handle_starttag(self, tag, attrs):
        self._in_heading = tag == "h2"

    def handle_endtag(self, tag):
        if tag == "h2":
            self._in_heading = False

    def handle_data(self, data):
        if self._in_heading:
            self.headings.append(data.strip())


class SkillPackageTests(unittest.TestCase):
    def test_each_skill_contains_its_own_references_and_calculator(self):
        for root in (CHAT_SKILL, REPORT_SKILL):
            with self.subTest(skill=root.name):
                self.assertTrue((root / "SKILL.md").is_file())
                self.assertTrue((root / "agents/openai.yaml").is_file())
                self.assertTrue((root / "scripts/valuation.py").is_file())
                self.assertEqual(
                    {path.name for path in (root / "references").glob("*.md")},
                    REFERENCE_FILES,
                )

    def test_report_template_renders_required_offline_sections(self):
        template = (REPORT_SKILL / "assets/report-template.html").read_text(encoding="utf-8")
        replacements = {
            "TITLE": "Test valuation",
            "SUBTITLE": "Test subtitle",
            "AS_OF_LABEL": "ข้อมูล ณ วันที่",
            "AS_OF_DATE": "2026-09-07",
            "FRESHNESS_FLAG": "FRESH",
            "OVERVIEW_HEADING": "ภาพรวม",
            "OVERVIEW": "overview body",
            "DATA_HEADING": "ข้อมูลที่ใช้",
            "DATA": "data body",
            "VALUATION_HEADING": "การประเมินมูลค่า",
            "VALUATION": "valuation body",
            "SCENARIOS_HEADING": "สถานการณ์จำลอง",
            "SCENARIOS": "scenarios body",
            "RISKS_HEADING": "ความเสี่ยงสำคัญ",
            "RISKS": "risk body",
            "BOTTOM_LINE_HEADING": "สรุป",
            "BOTTOM_LINE": "bottom line body",
            "SOURCES_HEADING": "แหล่งข้อมูล",
            "SOURCES": "sources body",
        }
        for name, value in replacements.items():
            template = template.replace(f"{{{{{name}}}}}", value)

        self.assertNotIn("{{", template)
        self.assertNotIn("http://", template)
        self.assertNotIn("https://", template)

        parser = HeadingParser()
        parser.feed(template)
        self.assertEqual(
            parser.headings,
            [
                "ภาพรวม",
                "ข้อมูลที่ใช้",
                "การประเมินมูลค่า",
                "สถานการณ์จำลอง",
                "ความเสี่ยงสำคัญ",
                "สรุป",
                "แหล่งข้อมูล",
            ],
        )
