import typing

def factory(a, /, b, *, c, d=4, *args, **kwargs):
    return (a, b, c, d, args, kwargs)

Alias: typing.TypeAlias = factory  # Rule triggers here

# Store original defaults
import inspect
orig = inspect.signature(factory)
print(f'Original defaults: {orig.parameters["d"].default}')

# Call via alias
try:
    result = Alias(1, 2, c=3, d=99, 4, 5, extra=6)
    print(f'Alias call result: {result}')
except Exception as e:
    print(f'{type(e).__name__}: {e}')

# Now simulate what happens if the fix breaks something
# But the alias is just a function reference - should be fine
# Hazard: if the rewrite somehow broke the binding
print(f'Alias is still callable: {callable(Alias)}')
print(f'Alias.__name__: {Alias.__name__}')
