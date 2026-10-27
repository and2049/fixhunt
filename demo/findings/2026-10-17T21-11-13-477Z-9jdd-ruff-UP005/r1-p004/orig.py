import unittest
class CustomTestCase(unittest.TestCase):
    def assertEquals(self, a, b):
        print('Custom assertEquals called with', a, b)
        return super().assertEqual(a, b)
class Test(CustomTestCase):
    def test(self):
        self.assertEquals(1, 1)
        self.assertEqual(2, 2)
Test().test()
