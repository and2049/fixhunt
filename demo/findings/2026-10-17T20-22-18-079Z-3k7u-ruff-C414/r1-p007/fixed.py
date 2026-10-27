TMP = list(tuple([1, 2, 3]))
def func(x=TMP):
    return x
print(f'Default arg: {func()}')
TMP = ['changed']
print(f'After reassignment: {func()}')
