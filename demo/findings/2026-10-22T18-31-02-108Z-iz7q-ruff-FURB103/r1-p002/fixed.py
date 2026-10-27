import pathlib
results = []
for i in range(2):
    pathlib.Path(f'file{i}.txt').write_text(str(i))
    results.append(lambda: open(f'file{i}.txt').read())
print([r() for r in results])
for i in range(2):
    if os.path.exists(f'file{i}.txt'):
        os.remove(f'file{i}.txt')
