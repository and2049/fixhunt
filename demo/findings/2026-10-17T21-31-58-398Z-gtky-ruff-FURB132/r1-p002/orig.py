x = 1
s = {1, 2}
if x in s:
    x = 2  # reassigned before remove
    s.remove(x)  # removes 2, not original 1
print('Set after:', s)
print('x:', x)
