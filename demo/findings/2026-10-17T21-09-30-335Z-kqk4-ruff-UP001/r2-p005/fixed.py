# Now define a class that relies on this binding being visible
exec('''
class DynamicClass:
    __metaclass__ = type  # Should resolve to module __metaclass__
    attr = 'value'
''')
# Check if the class got the attribute
print('attr in DynamicClass:', hasattr(DynamicClass, 'attr'))
print('attr value:', getattr(DynamicClass, 'attr', 'missing'))
