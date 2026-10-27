class C:
    __metaclass__ = type
    def method(self): pass

try:
    C().method()
    print('method called')
except Exception as e:
    print(type(e).__name__ + ':', str(e))
