pairs = [(1, 2), (3, 4)]
try:
    d = dict(pairs)
    raise ValueError('bad')
except ValueError as e:
    print('caught:', e)
finally:
    print('finally block')
print('d exists:', 'd' in locals())
