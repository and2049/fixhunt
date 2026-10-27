import unittest
class Test(unittest.TestCase):
    def test(self):
        val = 1.0 / 3.0
        try:
            self.assertAlmostEquals(val, 0.333, places=5)
            print('assertAlmostEquals passed')
        except AssertionError as e:
            print('AssertionError:', type(e).__name__, str(e))
        self.assertAlmostEqual(val, 0.333, places=5)
        print('assertEqual passed')
Test().test()
