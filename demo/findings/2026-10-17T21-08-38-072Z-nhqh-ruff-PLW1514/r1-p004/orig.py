import sys
# Create two-line file: first line valid UTF-8, second has raw byte
with open('data.txt', 'wb') as f:
    f.write(b'key1\n\xff\n')
try:
    with open('data.txt', 'r') as f:  # Rule triggers: adds encoding='utf-8'
        lines = f.readlines()
    d = {}
    for i, line in enumerate(lines):
        try:
            d[f'key{i}'] = line.strip()
        except:
            pass  # Skip failed lines
    print('dict items:', list(d.items()))
except UnicodeDecodeError as e:
    print('decode error:', type(e).__name__, e)
finally:
    import os
    try: os.remove('data.txt')
    except: pass
