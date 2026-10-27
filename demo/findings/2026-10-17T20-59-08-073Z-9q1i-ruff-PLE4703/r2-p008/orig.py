def get_set():
    print('get_set called')
    return {1, 2}
s = get_set()
for x in s:
    print('x:', x)
    s.clear()
print('final s:', s)
