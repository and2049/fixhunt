pairs = [('a', 1), ('b', 2), ('c', 3)]
extra = [10, 20, 30, 40]  # ignore 40
try:
    results = list(map(lambda p, e: (p[0], p[1] + e), pairs, extra))
    print('results:', results)
except ValueError as e:
    print('ValueError:', e)
