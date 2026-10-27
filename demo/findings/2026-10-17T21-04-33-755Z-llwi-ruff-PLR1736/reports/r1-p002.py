lst = [10, 20]
for i, x in enumerate(lst):
    print(f'Before: lst[{i}]={lst[i]}, x={x}')
    if i == 0:
        lst = [99, 88]  # Rebinding in outer scope
