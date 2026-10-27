from typing import cast
# Already quoted with single quotes - rule may not fire (config-dependent)
def main():
    x = 42
    # This uses single quotes - depending on ruff config, TC006 may or may not trigger
    # We assume it does NOT trigger (as per rule description: stays silent on single quotes)
    y = cast('int', x)  # No trigger expected
    print('Value:', y, type(y))
    # If the rule incorrectly fired and added outer quotes:
    # cast(''int'', x) -> invalid syntax
    # We simulate the broken code
    try:
        # This line is commented out to avoid syntax error in our program
        # z = cast(''int'', x)  # SyntaxError: invalid syntax
        pass
    except SyntaxError as e:
        print('Simulated broken fix would cause:', type(e).__name__, str(e))
    # Show that single-quoted string is fine at runtime
    if isinstance(y, int):
        print('Single-quoted cast worked as expected')
if __name__ == '__main__':
    main()
