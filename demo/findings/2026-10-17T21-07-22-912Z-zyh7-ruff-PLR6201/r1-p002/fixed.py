bdata = b'hello\nworld'
sdata = bdata.decode()
for chunk in [b'hello\n', b'world']:
    before = chunk in [b'hello\n', b'world']
    after  = chunk in {b'hello\n', b'world'}
    print(f'Before: {chunk!r} in list -> {before}')
    print(f'After:  {chunk!r} in set  -> {after}')
    if before != after:
        print('  DIFFERENCE DETECTED')
