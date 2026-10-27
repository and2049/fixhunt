results = []
for i in range(2):
    s = f'0b{i}'
    if (val := int(s[2:], 2)) is not None:
        results.append(val)
print(results)
