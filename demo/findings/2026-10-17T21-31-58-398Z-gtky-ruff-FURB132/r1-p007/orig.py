s = {1, 2, 3}
removed = []
if 2 in s:
    s.remove(2)
    removed.append(2)
if len(s) == 2:  # invariant: expected size after removal
    print('Invariant holds')
else:
    print('Invariant broken:', s)
print('Removed list:', removed)
