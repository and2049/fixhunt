with open('tmp.bin', 'wb') as f:
    f.write(b'hello\nworld')
with open('tmp.bin', 'rb') as f:
    lines = {i: line for i, line in enumerate(f)}
    for idx, _ in lines.items():
        print(idx, end='')
