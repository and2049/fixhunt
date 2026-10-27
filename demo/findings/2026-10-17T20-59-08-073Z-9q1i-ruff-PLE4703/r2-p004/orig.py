s = {1, 2}
try:
    for x in s:
        if x == 1:
            raise ValueError('bad')
        s.discard(x)
except ValueError as e:
    print('ValueError:', type(e).__name__, str(e))
else:
    print('no exception')
finally:
    print('final set:', s)
