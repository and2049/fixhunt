lst = [1, 2, 3]
for i, x in enumerate(lst):
    if (tmp := lst[i]) > 0:
        tmp *= 2
    else:
        tmp = 0
    print(f'i={i}, tmp={tmp}', end=' ')
print()
