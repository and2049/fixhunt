class VerboseProperty:
    def __get__(self, obj, owner):
        print(f'Accessed by {obj}')
        return 42
class H(metaclass=abc.ABCMeta):
    x = VerboseProperty()
    @property
    def y(self):
        print('in y getter')
        return self._y
    def __init__(self):
        self._y = 99
print('Accessing h.x:')
h = H()
val = h.x
print(f'Got: {val}')
print('Accessing h.y:')
val2 = h.y
print(f'Got: {val2}')
