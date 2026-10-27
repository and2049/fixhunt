with open('test.bin', 'wb') as f:
    f.write(bytes(b'hello\n'))
with open('test.bin', 'rb') as f:
    print(f.read())
