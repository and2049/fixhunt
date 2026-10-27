state = []
def side_effect_func(x):
    state.append(x)
    if len(state) > 2:
        raise RuntimeError('too many')
    return x * 2
try:
    list(map(side_effect_func, [1, 2, 3], [10, 20]))
except ValueError as e:
    print('ValueError:', e)
except RuntimeError as e:
    print('RuntimeError:', e)
print('state:', state)
