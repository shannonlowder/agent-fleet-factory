import datetime as dt
import pathlib
import unittest

from check_landscape_date import check, main

D = dt.date(2026, 11, 27)
PAGE = "# Landscape\n\n**Last searched: 2026-11-27.** The search covered...\n"


class CheckLandscapeDate(unittest.TestCase):
    def test_fresh_date_passes(self):
        self.assertTrue(check(PAGE, D)[0])

    def test_exactly_at_limit_passes(self):
        self.assertTrue(check(PAGE, D + dt.timedelta(days=30))[0])

    def test_stale_date_fails(self):
        ok, msg = check(PAGE, D + dt.timedelta(days=31))
        self.assertFalse(ok)
        self.assertIn("31 days", msg)
        self.assertIn("Re-run the landscape search", msg)

    def test_missing_line_fails(self):
        self.assertFalse(check("# Landscape\n\nNo date here.\n", D)[0])

    def test_invalid_date_fails(self):
        self.assertFalse(check("**Last searched: 2026-13-40.**\n", D)[0])

    def test_future_date_fails(self):
        self.assertFalse(check(PAGE, D - dt.timedelta(days=1))[0])

    def test_repo_page_passes_on_its_search_date(self):
        page = pathlib.Path(__file__).resolve().parents[1] / "docs" / "landscape.md"
        self.assertEqual(main(["--file", str(page), "--today", "2026-11-27"]), 0)


if __name__ == "__main__":
    unittest.main()
