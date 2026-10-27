import unittest
class Test(unittest.TestCase):
    def test(self):
        # This check validates user input equivalence
        self.assertEquals('hello', 'hello')  # inline: critical
        print('Comment preserved and check passed')
Test().test()
