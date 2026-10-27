text = 'hello\nworld'
encoded = text.encode('utf-8')
print(repr(text))
print(repr(encoded))
with open('tmp.bin', 'wb') as f:
    f.write(encoded)
with open('tmp.bin', 'rb') as f:
    print(f.read())
