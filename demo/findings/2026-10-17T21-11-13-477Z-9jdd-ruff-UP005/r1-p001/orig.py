import unittest
class Test(unittest.TestCase):
    def test(self):
        data = [1, 2, 3]
        results = [(x := i) for i in data if self.assertEquals(x, i)]
        print('results:', results)
        print('final x:', x)
Test().test()
