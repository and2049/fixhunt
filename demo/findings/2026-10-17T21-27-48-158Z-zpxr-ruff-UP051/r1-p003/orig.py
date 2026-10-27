import abc
value = 123
try:
    exec('@abc.abstractproperty\nvalue')
except SyntaxError as e:
    print('SyntaxError:', type(e).__name__, str(e))
