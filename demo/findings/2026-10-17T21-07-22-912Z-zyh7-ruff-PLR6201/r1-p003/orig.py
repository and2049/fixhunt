values = [1, 1, 2]
count_before = 0
count_after  = 0
for v in values:
    if v in [1, 1, 2]:
        count_before += 1
    if v in {1, 1, 2}:
        count_after += 1
print(f'Before (list): {count_before} matches')
print(f'After  (set):  {count_after} matches')
if count_before != count_after:
    print('  COUNT CHANGED: duplicates collapsed in set')
