name = 'foo'
value = 42
# These do NOT trigger B043 (not literals)
delattr_test = lambda obj, attr: delattr(obj, attr)
class O:
    pass
o = O()
setattr(o, name, value)
print('Before:', getattr(o, name))
delattr(o, name)  # rule does NOT fire — variable
print('After:', getattr(o, name, 'missing'))
# Now a literal that DOES trigger
setattr(o, 'bar', 'baz')
del o.bar  # rule fires here
print('bar after del:', getattr(o, 'bar', 'missing'))
