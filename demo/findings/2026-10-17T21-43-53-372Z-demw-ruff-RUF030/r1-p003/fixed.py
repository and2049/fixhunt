def f(x, lst=[]):
    lst.append(x)
    return lst
results = []
for i in [1, 2]:
    try:
        assert i < 2, print(f(i))
    except AssertionError as e:
        results.append(str(e))
    else:
        results.append('no raise')
print('|'.join(results))
