items = []
for x in {'a', 'b'}:
    items.append(x.upper())
rebuilt = set(items)
print(''.join(sorted(rebuilt)))
