from typing import cast
# Mistakenly using tuple as type - should be flagged by linter but isn't a type
def main():
    x = (1, 'hello')
    # This is wrong: (int, str) is a tuple, not a type
    # Rule TC006 should fire because it's unquoted
    y = cast((int, str), x)  # Expect trigger: first arg is tuple literal
    print('Cast result:', y, type(y))
    # At runtime, this succeeds because cast ignores the type argument
    # But if we later try to use (int, str) as a type in isinstance, it fails
    try:
        if isinstance(y, (int, str)):  # This works: tuple of types
            print('isinstance check passed')
        else:
            print('isinstance check failed')
    except Exception as e:
        print('Error in isinstance:', type(e).__name__, str(e))
    # After fix: cast('(int, str)', x) -> first arg becomes string
    # Now, if code later tried to evaluate the string as a type (e.g. via eval), it would fail
    # But more importantly, the linter fix masks the error: the user thinks it's quoted on purpose
    # So they don't realize (int, str) was never a valid type
    try:
        eval_type = eval('(int, str)')  # This would work
        print('Eval succeeded:', eval_type)
    except Exception as e:
        print('Eval error:', type(e).__name__, str(e))
if __name__ == '__main__':
    main()
