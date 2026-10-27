def write_all(f, sep=',', *, end='\n'):
    for x in [1, 2, 3]:
        f.write(str(x) + sep)
    f.write(end)
f = open('tmp.txt', 'w')
write_all(f, sep='|')
f.close()
print(repr(open('tmp.txt').read()))
