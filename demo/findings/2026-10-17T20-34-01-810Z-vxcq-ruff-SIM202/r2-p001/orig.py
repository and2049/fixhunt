def f():
    x, y = 1, 2
    cond = True
    z = 99
    result = (not x != y) if cond else z
    print('orig:', result)
    # After fix: becomes x == y if cond else z
    result_fixed = (x == y) if cond else z
    print('fixed:', result_fixed)
    assert result == result_fixed
f()
