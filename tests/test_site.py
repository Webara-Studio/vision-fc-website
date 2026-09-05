import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SiteSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text()
        cls.css = (ROOT / "styles.css").read_text()
        cls.js = (ROOT / "app.js").read_text()

    def test_required_runtime_files_exist(self):
        for relative in (
            "styles.css",
            "app.js",
            "assets/players.json",
            "brand-guide.pdf",
            "intro-video.mp4",
            "robots.txt",
            "sitemap.xml",
            "vercel.json",
            "local-fonts.css",
            "fonts/barlow-condensed-0.ttf",
            "assets/crest-transparent.webp",
            "assets/crest-transparent-320.webp",
            "assets/nii-adjei-kraku-ii-optimised.jpg",
            "assets/nii-adjei-kraku-ii-800.webp",
            "assets/nii-adjei-kraku-ii-400.webp",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_html_uses_external_runtime_layers(self):
        self.assertIn('<link rel="stylesheet" href="styles.css">', self.html)
        self.assertIn('<script src="app.js" defer></script>', self.html)
        self.assertNotIn("<style>", self.html)
        self.assertNotIn("<script>", self.html)

    def test_critical_links_and_seo_markers_remain(self):
        for marker in (
            'rel="canonical"',
            'application/ld+json',
            'og:image',
            'site.webmanifest',
            'href="brand-guide.pdf" download',
            'data-open-video',
            'intro-video.mp4',
        ):
            self.assertIn(marker, self.html)
        header = self.html.split("<main", 1)[0]
        footer = self.html.split("<footer", 1)[1].split("</footer>", 1)[0]
        self.assertNotIn("brand-guide.pdf", header)
        self.assertIn("brand-guide.pdf", footer)

    def test_player_data_is_valid_and_behaviour_is_externalised(self):
        players = json.loads((ROOT / "assets/players.json").read_text())
        self.assertEqual(len(players), 16)
        self.assertTrue(all(isinstance(player, str) for player in players))
        self.assertIn("assets/players.json", self.js)
        self.assertIn("async function loadPlayers", self.js)

    def test_motion_and_accessibility_fallback_remain(self):
        self.assertIn("@keyframes crestFloat", self.css)
        self.assertIn("prefers-reduced-motion", self.css)
        self.assertIn("prefers-reduced-motion", self.js)
        self.assertIn('aria-modal="true"', self.html)

    def test_no_inline_event_handlers(self):
        self.assertIsNone(re.search(r"\bon(click|input|change|submit)=", self.html, re.I))


if __name__ == "__main__":
    unittest.main()
