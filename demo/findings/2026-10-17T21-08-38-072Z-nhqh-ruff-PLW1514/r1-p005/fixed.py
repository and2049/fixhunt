import sys
# Create UTF-16 LE file with BOM
with open('msg.txt', 'wb') as f:
    f.write(b'\xff\feH\x00e\x00l\x00l\x00o\x00')
try:
    with open('msg.txt', 'r') as f:  # Rule triggers: adds encoding='utf-8' -> decodes UTF-16 as UTF-8 -> garbage
        s = f.read()
    formatted = 'Message: %s' % s
    print('formatted:', formatted)
except Exception as e:
    print('error:', type(e).__name__, e)
finally:
    import os
    try: os.remove('msg.txt')
    except: pass
