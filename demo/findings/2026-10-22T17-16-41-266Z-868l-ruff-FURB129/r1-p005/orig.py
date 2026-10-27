with open('tmp.bin', 'wb') as f:
    f b'hello\nworld'

with open('tmp.bin', 'rb') as fp:
    trace = []
    for line in fp.readlines():  # Rule triggers here
        try:
            trace.append(line.decode().strip())
        except AttributeError as e:
            trace.append(f'DECODE_ERR:{type(e).__name__}')
        if len(trace) >= 2:
            break
print('|'.join(trace))
