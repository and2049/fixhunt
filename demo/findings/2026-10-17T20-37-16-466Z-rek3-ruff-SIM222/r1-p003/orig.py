def append_val(val, lst=None):
    if lst is None:
        lst = val or []  # Rule may fire here
    lst.append(val)
    return lst

print('append_val(1):', append_val(1))
print('append_val(2):', append_val(2))
print('append_val(3):', append_val(3))

# Expected: each call returns [1], [2], [3]
# If rewritten to `lst = []`, then all calls share same list: [1, 2, 3]
