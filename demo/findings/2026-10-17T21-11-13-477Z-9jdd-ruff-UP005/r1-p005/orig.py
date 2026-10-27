import unittest
import functools
class Test(unittest.TestCase):
    def test(self):
        func = functools.partial(getattr(self, 'assertEquals'), 1)
        try:
            func(1)
            print('Success')
        except AttributeError as e:
            print('AttributeError:', type(e).__name__, str(e))
Test().test()
