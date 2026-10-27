f = open('tmp.txt', 'w')
snapshots = []
for x in ['a', 'b']:
    f.write(x)
    snapshots.append(x)
    x = 'mutated'
f.close()
with open('tmp.txt') as f:
    content = f.read()
print('file wrote:', content)
print('x after write:', snapshots)
