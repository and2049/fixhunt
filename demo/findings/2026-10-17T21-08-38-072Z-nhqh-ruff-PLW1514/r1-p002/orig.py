import sys
# Create a file encoded in Windows-1252 (contains euro symbol \x80)
with open('test.txt', 'wb') as f:
    f.write(b'Hello \x80 World')  # € in CP1252
# Original behavior: uses system default (assumed CP1252 here)
try:
    with open('test.txt', 'r') as f:  # Rule triggers: adds encoding='utf-8'
        content = f.read()
    print('read success:', repr(content))
except UnicodeDecodeError as e:
    print('read failed:', type(e).__name__, e)
except Exception as e:
    print('other error:', type(e).__name__, e)
finally:
    import os
    try: os.remove('test.txt')
    except: pass
