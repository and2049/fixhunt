import sys
if sys.version_info < (3, 12):
    print('SKIP: Target version < 3.12, but we still write the code to be fixed')
    # Simulate what the fix would produce: invalid syntax in <3.12
    # We cannot actually run invalid syntax, so we show the intent
    # The rule would rewrite this to `type T = int` which is invalid
    T: typing.TypeAlias = int  # This line is what the rule sees
    try:
        # This would fail after fix in <3.12
        reveal_type(T)  # type: ignore
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
else:
    T: typing.TypeAlias = int
    print(f'T is {T} and type(T) is {type(T)}')
