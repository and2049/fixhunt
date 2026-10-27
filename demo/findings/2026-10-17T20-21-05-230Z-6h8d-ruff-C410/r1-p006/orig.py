def process_tuple(t):
    return list(t)
result = process_tuple((1, 2, 3))
print('List from tuple:', result)
try:
    process_tuple('not a tuple')
except TypeError as e:
    print('Caught TypeError:', e)
