mapping = {'a': 'hello', 'b': 'world'}  # b unused
part = 'Hello %(a)s' % mapping
combined = part + str(len(mapping))  # len depends on full dict
print('Combined:', combined)
# After fix: mapping becomes {'a': 'hello'}, len=1 -> 'Hello hello1'
# Before: len=2 -> 'Hello hello2'
