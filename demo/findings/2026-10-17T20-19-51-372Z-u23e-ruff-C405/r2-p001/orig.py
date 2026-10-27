outer_list = []
for i in range(2):
    lst = [i]
    outer_list.append(lst)
    s = set(lst)
    lst[0] = 99
    print(f'i={i}, set={s}, lst={lst}')
