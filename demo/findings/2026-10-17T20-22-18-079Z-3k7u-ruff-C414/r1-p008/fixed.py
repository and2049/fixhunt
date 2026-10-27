get_pair = lambda: [1, 2]
result = list(tuple(get_pair()))
print(f'Result: {result}')
try:
    broken = list(get_pair)  # What the buggy fix would produce
    print(f'Broken: {broken}')
except TypeError as e:
    print(f'{type(e).__name__}: {e}')
