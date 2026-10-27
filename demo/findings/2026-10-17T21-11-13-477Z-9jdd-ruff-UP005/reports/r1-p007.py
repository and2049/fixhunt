import unittest
class Test(unittest.TestCase):
    def test(self):
        self.assertEquals('hello', 'hello')  # inline: critical
Test().test()
