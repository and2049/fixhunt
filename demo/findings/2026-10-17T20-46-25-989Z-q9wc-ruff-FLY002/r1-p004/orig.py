def make_pair(lst=None):
    if lst is None:
        lst = []
    lst.extend(['a', 'b'])
    return lst
pair1 = make_pair()
pair2 = make_pair()
sep = ' '
joined = sep.join(pair1)
fstringed = f'{pair1[0]} {pair1[1]}'
print(f'{joined}|{fstringed}')
# Show aliasing
pair1.clear()
print(len(pair2))
