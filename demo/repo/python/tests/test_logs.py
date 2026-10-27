import tempfile
import unittest
from pathlib import Path

from toolbox import has_duplicate


class LogTests(unittest.TestCase):
    def test_duplicate_after_first_line(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "keys.log"
            p.write_text("alpha\nbeta\nbeta\n")
            self.assertTrue(has_duplicate(p))

    def test_no_duplicate(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "keys.log"
            p.write_text("alpha\nbeta\n")
            self.assertFalse(has_duplicate(p))
