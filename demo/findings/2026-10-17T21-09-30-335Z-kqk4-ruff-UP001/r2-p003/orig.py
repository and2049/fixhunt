class FormatTest:
    __metaclass__ = type
    s = 'hello'
    # Test various string formatting that might be affected by namespace
    pct = '%s world' % s
    fmt = '{} world'.format(s)
    fstr = f'{s} world'
    # Ensure these are computed correctly
    print(repr(pct), repr(fmt), repr(fstr))
    assert pct == fmt == fstr == 'hello world'
