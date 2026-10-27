import unittest
from typing import get_type_hints
class Test(unittest.TestCase):
    def method(self) -> 'assertEquals(1, 1)':
        pass
class TestSub(Test):
    def test(self):
        hints = get_type_hints(self.method, include_extras=True)
        print('hints:', hints)
        try:
            self.assertEquals(1, 1)
        except AttributeError as e:
            print('AttributeError:', type(e).__name__, str(e))
TestSub().test()
