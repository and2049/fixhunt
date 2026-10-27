from typing import cast, List
list = str  # Shadow builtin
T = list  # Now T is str
def main():
    x = 'hello'
    # First use: T refers to shadowed list (which is str)
    y = cast(T, x)  # Should be cast(str, x)
    print('After cast:', y.upper() if isinstance(y, str) else 'fail')
    # Later, redefine list back to builtin
    del list  # Restore builtin
    list = lambda x: x  # Redefine as identity
    T = list  # Now T is the lambda
    z = cast(T, x)  # cast(lambda, x) -> invalid type
    try:
        # This won't fail at runtime, but type checker will complain
        print('z:', z)
    except Exception as e:
        print('Error after redefinition:', type(e).__name__, str(e))
if __name__ == '__main__':
    main()
