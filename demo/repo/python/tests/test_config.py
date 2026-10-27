import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from toolbox import save, save_count


class ConfigTests(unittest.TestCase):
    def test_save_disabled_writes_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "settings.ini"
            save(p, "debug=1\n", enabled=False)
            self.assertEqual(p.read_text(), "")

    def test_save_enabled_writes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "settings.ini"
            save(p, "debug=1\n", enabled=True)
            self.assertEqual(p.read_text(), "debug=1\n")

    def test_save_count_prints_length(self):
        with tempfile.TemporaryDirectory() as d:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                save_count(Path(d) / "x.txt", "abc")
            self.assertEqual(out.getvalue(), "3\n")
