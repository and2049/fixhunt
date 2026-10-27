import unittest
import sys
# Simulate IPython reload: restore deprecated alias after import
if 'unittest' in sys.modules:
    unittest.TestCase.assertEquals = lambda self, a, b: self.assertEqual(a, b)
class Test(unittest.TestCase):
    def test(self):
        try:
            self.assertEquals(1, 1)
            print('Success via restored alias')
        except AttributeError as e:
            print('AttributeError:', type(e).__name__, str(e))
Test().test()
