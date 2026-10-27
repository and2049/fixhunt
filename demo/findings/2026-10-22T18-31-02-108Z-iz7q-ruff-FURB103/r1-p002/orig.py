results = []
for i in range(2):
    with open(f'file{i}.txt', 'w') as f:
        f.write(str(i))
    results.append(lambda: open(f'file{i}.txt').read())
print([r() for r in results])
for i in range(2):
    if os.path.exists(f'file{i}.txt'):
        os.remove(f'file{i}.txt')
