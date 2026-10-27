with open('tmp.txt', 'w') as f:
    f.write(b'abc')
with open('tmp.txt', 'r') as f:
    print(f.read())
