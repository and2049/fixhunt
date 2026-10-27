calls = []
def key_fn(x):
    calls.append(('key', x))
    return x
data = [3, 1, 2]
sorted_once = sorted(data, key=key_fn)
list_wrapped = list(sorted_once)
print('Key call log:', calls)
print('List wrapped:', list_wrapped)
print('Same as sorted?', list_wrapped == sorted_once)
