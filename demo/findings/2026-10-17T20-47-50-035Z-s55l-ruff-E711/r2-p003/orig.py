def test():
    None = 5  # Shadow built-in None
    x = 5
    try:
        if x == None:  # Rule triggers: compares x == 5 -> True
            print('eq_true')
        else:
            print('eq_false')
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
    # After broken fix: becomes 'x is 5' -> True (same value, but still wrong intent)
    # But we show the original behavior is preserved in this version
    # The hazard is that the fix would break meaning — we show what the fix would do
    # by simulating the incorrect rewrite
    try:
        if x is None:  # This is what the buggy fix would produce
            print('is_true')
        else:
            print('is_false')
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
test()
