f = open('tmp.txt', 'w')
results = []
for x in [b'a', b'b']:
    n = f.write(x)
    results.append(n)
f.close()
with open('tmp.txt') as f: content = f.read()
print('write returns:', results)
print('file content:', repr(content))
