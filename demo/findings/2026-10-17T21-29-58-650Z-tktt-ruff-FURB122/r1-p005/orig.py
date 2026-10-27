f = open('tmp.txt', 'w')
written = []
for x in [1, 2, 3]:
    if x % 2 == 1:
        f.write(str(x))
        written.append(x)
f.close()
with open('tmp.txt') as f:
    content = f.read()
print('conditioned writes:', written)
print('file content:', repr(content))
