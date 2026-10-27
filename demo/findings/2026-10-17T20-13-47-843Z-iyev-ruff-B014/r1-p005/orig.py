try:
    int('x')
except (Exception, ValueError) as e:
    if isinstance(e, ValueError):
        print('value error path')
    else:
        print('other error:', type(e).__name__)
