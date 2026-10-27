
gen = (c for c in 'café'.encode())  # UP012 triggers here
first = list(gen)
second = list(gen)  # exhausted!
print(f'{len(first)} {len(second)}')
if len(second) == 0:
    print('generator exhausted after first use')
else:
    print('unexpected: generator reusable')
