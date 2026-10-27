class MyClass: pass
x = MyClass()
try:
    result = isinstance(x, ('MyClass', int))
    print('Before:', result)
except Exception as e:
    print('Before error:', type(e).__name__, str(e))
