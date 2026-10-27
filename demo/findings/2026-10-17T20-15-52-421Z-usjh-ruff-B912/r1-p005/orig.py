effects = []
def side(x):
    effects.append(x)
    return x * 2
try:
    list(map(side, [1, 2, 3], [4, 5]))  # mismatched lengths
    print('effects:', effects)
except ValueError as e:
    print('ValueError:', str(e))
    print('effects so far:', effects)
