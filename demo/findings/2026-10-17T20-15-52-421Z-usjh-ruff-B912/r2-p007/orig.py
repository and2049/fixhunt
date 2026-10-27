def make_map(args_list):
    return lambda f, *iters: list(map(f, *iters, *args_list))
args_provider = [[]]  # empty
mapper = make_map(args_provider)
try:
    result = mapper(pow, [2, 3], [3, 2])
    print('result:', result)
except ValueError as e:
    print('ValueError:', e)
