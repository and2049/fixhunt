import unittest
class Test(unittest.TestCase):
    def test(self):
        method_name = 'assertEquals'
        method = getattr(self, method_name)
        try:
            method(1, 1)
            print('Success')
        except AttributeError as e:
            print('AttributeError:', type(e).__name__, str(e))
Test().test()
