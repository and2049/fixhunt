with open('tmp.txt', 'w') as f:
    f.write(b'abc')
if 0:
    pass
with open('tmp.txt', 'r') as f:
    print(f.read())
