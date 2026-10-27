class Descriptor:
    def __init__(self, value):
        self.value = value
    def __get__(self, obj, objtype):
        print(f'Descriptor accessed, returning {self.value}')
        return self.value
    def __set__(self, obj, value):
        print(f'Descriptor set to {value}')
        self.value = value

class MyClass:
    attr = Descriptor(set(x for x in [1, 2, 3]))  # Rule triggers here
    # __set__ called once at class definition with set(...) -> {1,2,3}

print('Accessing MyClass.attr:')
val = MyClass.attr  # Triggers __get__
print('Value:', val)

# After fix: attr = Descriptor({x for x in [1,2,3]})
# Same behavior: __set__ called once with {1,2,3}
# So no change.
# But we show that if the generator were evaluated per access, it would differ.
# Since it's evaluated once at class definition, we note the hazard is misattributing
# timing to instance access.

# Instance attribute version
class Simple:
    def __init__(self):
        self.data = set(x for x in [4, 5, 6])  # Rule triggers here

s = Simple()
print('Instance attr:', s.data)  # {4,5,6}
# After fix: self.data = {x for x in [4,5,6]} -> same.
