x = 5
if type(x) is type(None):  # this comment should be preserved
    print('unreachable')
else:
    print('x is not None:', x)
