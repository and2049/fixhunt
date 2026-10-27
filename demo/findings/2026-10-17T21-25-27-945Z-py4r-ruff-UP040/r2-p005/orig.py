import typing

T: typing.TypeAlias = int  # Rule triggers here

x = 42
print(f'isinstance(x, T) before any fix: {isinstance(x, T)}')
print(f'type(T): {type(T)}')
print(f'T is: {T}')

# After fix: `type T = int` -> T becomes a type, but cannot be used in isinstance at runtime?
# Actually, in 3.12+, `type T = int` makes T a type and usable in isinstance.
# But the hazard is: the rule removes the *variable*, so if code relied on T being a variable...
# Let's test if T is callable or has id
print(f'id(T): {id(T)}')
try:
    T()  # Try to call it as if it were a constructor from a variable
    print('T() succeeded')
except Exception as e:
    print(f'T() failed: {type(e).__name__}: {e}')
