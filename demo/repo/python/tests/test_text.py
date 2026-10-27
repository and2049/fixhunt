import tempfile
import unittest
from pathlib import Path

from toolbox import present, shout
from toolbox.text import read_first


class TextTests(unittest.TestCase):
    def test_present(self):
        self.assertEqual(present({"a": 1, "b": 2}, {"b"}), ["b"])

    def test_shout(self):
        self.assertEqual(shout(["hi"]), ["HI!"])

    def test_read_first(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "f.txt"
            p.write_text("one\ntwo\n")
            self.assertEqual(read_first(p), "one")
