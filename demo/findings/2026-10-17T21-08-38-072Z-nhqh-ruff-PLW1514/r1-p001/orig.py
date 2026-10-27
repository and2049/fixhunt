import sys
lines = [b'\xff\xfe']
def gen():
    for b in lines:
        yield b.decode('utf-16-le')
g = gen()
try:
    next(g)
except UnicodeDecodeError as e:
    print('gen failed:', type(e).__name__, e)
# Now simulate fixed code: open with encoding='utf-8' on binary data
try:
    with open('test.bin', 'wb') as f:
        f.write(b'\xff\xfe')
    with open('test.bin', 'r', encoding='utf-8') as f:  # Rule triggers here
        content = f.read()
    print('fixed read:', repr(content))
except Exception as e:
    print('fixed error:', type(e).__name__, e)
finally:
    import os
    try: os.remove('test.bin')
    except: pass
