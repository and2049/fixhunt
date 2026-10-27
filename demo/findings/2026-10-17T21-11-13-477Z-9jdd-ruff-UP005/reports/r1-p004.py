import unittest
class CustomTestCase(unittest.TestCase):
    def assertEquals(self, a, b):
        print('Custom assertEquals called with', a, b)
class Test(CustomTestCase):
    def test(self):
        self.assertEquals(1, 1)
Test().test()
