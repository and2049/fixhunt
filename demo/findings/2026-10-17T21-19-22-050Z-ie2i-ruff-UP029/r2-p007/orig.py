from past.builtins import map

result = map(lambda x: x*2, [1, 2, 3])
print('type:', type(result), 'list:', list(result))
