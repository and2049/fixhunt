items = [(1, 'a'), (2, 'b')]
expr = dict((k, v) for k, v in items) + [{'extra': 1}]
print('expr type:', type(expr))
print('expr length:', len(expr))
try:
    expr2 = {(k, v) for k, v in items} + [{'extra': 1}]
    print('comp expr type:', type(expr2))
    print('comp expr length:', len(expr2))
except TypeError as e:
    print('TypeError:', type(e).__name__, ':', str(e))
