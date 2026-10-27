class I(object):
    value = 42
    def __str__(self):
        return f'Value: {self.value}'
    def __repr__(self):
        return f'I({self.value!r})
'

i = I()
print(str(i))
print(repr(i))
