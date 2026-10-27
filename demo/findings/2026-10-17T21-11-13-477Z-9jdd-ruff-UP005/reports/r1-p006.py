import unittest
class Test(unittest.TestCase):
    def test(self):
        try:
            self.assertAlmostEquals(val, 0.333, places=5)
        except AssertionError as e:
            print('AssertionError:', type(e).__name__, str(e))
Test().test()
