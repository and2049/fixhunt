import typing

# Use a typing-only import that would be removed if not used
from typing import List  # This is used in the alias below

Mylist: typing.TypeAlias = List[int]  # Rule triggers here

# Force evaluation of the annotation at runtime
print(f'Mylist: {Mylist}')
print(f'type(Mylist): {type(Mylist)}')

# Now, if the rewrite happens, and we are in a context where typing is not imported...
# But we imported it above. So make it conditional
# Instead, test if the alias retains the ability to resolve List
try:
    # This should work because Mylist is a variable holding the resolved type
    x: Mylist = [1, 2]
    print(f'Variable annotation with Mylist: {x}')
except Exception as e:
    print(f'{type(e).__name__}: {e}')

# After fix: `type Mylist = List[int]` - in 3.12+ this is fine, but if someone
# deleted the import, it would break. But we didn't.
# So instead, show that the alias is usable as a type hint
print('Successfully used Mylist in type annotation')
