import typing

def outer():
    inner_T: typing.TypeAlias = list[str]  # Rule triggers here
    def inner():
        return inner_T  # After fix: `type inner_T = list[str]` - but is it visible?
    return inner()

try:
    result = outer()
    print(f'Outer returned: {result}')
    print(f'Isinstance check: {isinstance(["a"], result)}')
except Exception as e:
    print(f'{type(e).__name__}: {e}')
