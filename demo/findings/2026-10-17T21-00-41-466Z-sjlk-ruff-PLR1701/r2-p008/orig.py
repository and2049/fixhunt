data = b'hello\nworld'
if isinstance(data, bytes) or isinstance(data, str):
    print('is bytes or str')
    if isinstance(data, bytes):
        print(f'bytes len={len(data)}')
    else:
        print(f'str len={len(data)}')
else:
    print('neither')
