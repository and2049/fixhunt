class MyClass:
    def __init__(self):
        self._val = None
    
    @property
    def val(self):
        print('Property accessed')
        return self._val

obj = MyClass()
if type(obj.val) is type(None):
    print('obj.val is None')
else:
    print('obj.val is not None')
