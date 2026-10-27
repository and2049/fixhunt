class Data:
    def __init__(self):
        self._val = 0
    @property
    def val(self):
        self._val += 1
        return self._val
obj = Data()
mapping = {'value': obj.val, 'extra': obj.val}  # extra unused but triggers side effect
result = 'Value: %(value)d' % mapping
print('Result:', result)
print('Obj val after:', obj.val)
