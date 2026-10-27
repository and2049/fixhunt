def my_open(file, *, mode='r', encoding=None, **kwargs):
    if encoding is None and 'b' not in mode:
        encoding = 'utf-8'
    return open(file, mode=mode, encoding=encoding, **kwargs)

# Rule triggers on the open call inside my_open
try:
    with open('test.txt', 'w') as f:
        f.write('hello')
    # This call: my_open('test.txt', mode='r', buffering=-1)
    # Before fix: open('test.txt', mode='r', buffering=-1) -> encoding=None -> uses default
    # After fix: open('test.txt', mode='r', encoding='utf-8', buffering=-1) -> forces utf-8
    with my_open('test.txt', mode='r', buffering=-1) as f:
        content = f.read()
    print('read content:', repr(content))
except Exception as e:
    print('error:', type(e).__name__, e)
finally:
    import os
    try: os.remove('test.txt')
    except: pass
