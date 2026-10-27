import abc
ac = abc.abstractclassmethod
# Rule does not fire here; if it did incorrectly, fix would be invalid
@ac
    def fake_method(cls): pass
# Simulate what incorrect fix would produce: @classmethod\n@abc.abstractmethod\n# This would be valid syntax but semantically wrong—we test validity via try
try:
    exec('@classmethod\n@abc.abstractmethod\ndef fake_method(cls): pass')
    print('No syntax error from simulated fix')
except SyntaxError as e:
    print('SyntaxError from simulated fix:', type(e).__name__, str(e))
