foo = [1, 2, 3, 4]
result = []
def gen():
    for x in foo[:]:
        if x == 2:
            foo.remove(3)
        yield x
for x in list(x for x in gen()):
    result.append(x)
print(result)
