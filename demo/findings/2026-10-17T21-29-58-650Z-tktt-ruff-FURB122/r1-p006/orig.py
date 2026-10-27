def writer(items, lst=[]):
    f = open('tmp.txt', 'w')
    for x in items:
        f.write(str(x))
        lst.append(x)
    f.close()
    return lst
first = writer([1, 2])
second = writer([3, 4])
print('first call:', first)
print('second call:', second)
with open('tmp.txt') as f:
    print('file content:', repr(f.read()))
