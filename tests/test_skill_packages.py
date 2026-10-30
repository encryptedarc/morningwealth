from html.parser import HTMLParser
import json
import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHAT_SKILL = ROOT / "plugins/encryptedarc/skills/valuation-deep-dive"
REPORT_SKILL = ROOT / "plugins/encryptedarc/skills/valuation-deep-dive-html-report"
FUNDAMENTAL_SKILL = ROOT / "plugins/encryptedarc/skills/fundamental"
EARNINGS_SKILL = ROOT / "plugins/encryptedarc/skills/earnings"
SKILLS = (CHAT_SKILL, REPORT_SKILL, FUNDAMENTAL_SKILL, EARNINGS_SKILL)
REFERENCE_FILES = {
    "archetype-playbooks.md",
    "core-finance-principles.md",
    "data-sourcing-valuation.md",
    "dcf-and-cost-of-capital.md",
    "peer-calibration.md",
    "thai-market-notes.md",
}
FUNDAMENTAL_REFERENCE_FILES = {
    "fundamental-framework.md",
    "source-policy.md",
}
EARNINGS_REFERENCE_FILES = {
    "earnings-framework.md",
    "source-policy.md",
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
    def test_marketplace_resolves_to_plugin_and_bundled_skills(self):
        marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
        for entry in marketplace["plugins"]:
            with self.subTest(plugin=entry["name"]):
                plugin_dir = (ROOT / entry["source"]["path"]).resolve()
                self.assertIn(ROOT, plugin_dir.parents)
                manifest = json.loads(
                    (plugin_dir / ".codex-plugin/plugin.json").read_text(encoding="utf-8")
                )
                self.assertEqual(manifest["name"], entry["name"])
                skill_dir = (plugin_dir / manifest["skills"]).resolve()
                self.assertIn(plugin_dir, skill_dir.parents)
                self.assertEqual({p for p in skill_dir.iterdir() if p.is_dir()}, set(SKILLS))

    def test_skill_frontmatter_has_required_portable_fields(self):
        allowed = {"name", "description", "license", "metadata", "allowed-tools"}
        for skill in SKILLS:
            with self.subTest(skill=skill.name):
                content = (skill / "SKILL.md").read_text(encoding="utf-8")
                header = re.match(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
                self.assertIsNotNone(header, "Missing frontmatter block")
                fields = set(re.findall(r"^([a-z][a-z-]*):", header[1], re.MULTILINE))
                self.assertTrue({"name", "description"}.issubset(fields))
                self.assertFalse(fields - allowed, f"Nonportable fields: {fields - allowed}")
                name = re.search(r"^name: ([a-z0-9-]+)$", header[1], re.MULTILINE)
                self.assertIsNotNone(name)
                self.assertEqual(name[1], skill.name)

    def test_referenced_resources_are_bundled_inside_each_skill(self):
        for skill in SKILLS:
            for document in skill.rglob("*.md"):
                if "local" in document.relative_to(skill).parts:
                    continue
                content = document.read_text(encoding="utf-8")
                for resource in re.findall(r"(?:references|scripts|assets)/[\w./-]+\.(?:md|py|html)", content):
                    with self.subTest(skill=skill.name, document=document.name, resource=resource):
                        target = (skill / resource).resolve()
                        self.assertIn(skill, target.parents)
                        self.assertTrue(target.is_file(), f"Missing bundled resource: {resource}")

    def test_standalone_valuation_copies_remain_in_sync(self):
        for resource in ["scripts/valuation.py", *[f"references/{name}" for name in sorted(REFERENCE_FILES)]]:
            with self.subTest(resource=resource):
                self.assertEqual((CHAT_SKILL / resource).read_bytes(),
                                 (REPORT_SKILL / resource).read_bytes())

    def test_fundamental_skill_is_standalone_and_discoverable(self):
        self.assertTrue((FUNDAMENTAL_SKILL / "SKILL.md").is_file())
        self.assertTrue((FUNDAMENTAL_SKILL / "agents/openai.yaml").is_file())
        self.assertEqual(
            {path.name for path in (FUNDAMENTAL_SKILL / "references").glob("*.md")},
            FUNDAMENTAL_REFERENCE_FILES,
        )

    def test_fundamental_skill_package_contains_no_thai_instructions(self):
        text_files = [
            FUNDAMENTAL_SKILL / "SKILL.md",
            FUNDAMENTAL_SKILL / "agents/openai.yaml",
            *(FUNDAMENTAL_SKILL / "references").glob("*.md"),
        ]

        for path in text_files:
            with self.subTest(path=path.relative_to(ROOT)):
                content = path.read_text(encoding="utf-8")
                contains_thai = any("\u0e00" <= char <= "\u0e7f" for char in content)
                self.assertFalse(contains_thai, f"Thai instructions found in {path.relative_to(ROOT)}")

    def test_earnings_skill_is_standalone_and_discoverable(self):
        self.assertTrue((EARNINGS_SKILL / "SKILL.md").is_file())
        self.assertTrue((EARNINGS_SKILL / "agents/openai.yaml").is_file())
        self.assertEqual(
            {path.name for path in (EARNINGS_SKILL / "references").glob("*.md")},
            EARNINGS_REFERENCE_FILES,
        )

    def test_earnings_skill_package_contains_no_thai_instructions(self):
        text_files = [
            EARNINGS_SKILL / "SKILL.md",
            EARNINGS_SKILL / "agents/openai.yaml",
            *(EARNINGS_SKILL / "references").glob("*.md"),
        ]

        for path in text_files:
            with self.subTest(path=path.relative_to(ROOT)):
                content = path.read_text(encoding="utf-8")
                contains_thai = any("฀" <= char <= "๿" for char in content)
                self.assertFalse(contains_thai, f"Thai instructions found in {path.relative_to(ROOT)}")

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
