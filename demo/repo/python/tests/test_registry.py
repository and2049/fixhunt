import unittest

from toolbox import Registry, lookup, resolve


class RegistryTests(unittest.TestCase):
    def test_lookup_registered(self):
        reg = Registry()
        reg.register("db", "postgres")
        self.assertEqual(lookup(reg, "db"), "postgres")
        self.assertIsNone(lookup(reg, "cache"))

    def test_resolve_listed_names(self):
        table = {"a": ["b", "c"], "b": []}
        self.assertEqual(resolve(table), {"b": [], "c": None})
