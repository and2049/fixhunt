import os
if os.path.exists('tmp.bin'): os.remove('tmp.bin')
f = open('tmp.bin', 'wb')
try:
    for x in [b'hello', b'world']:
        f.write(x)
except Exception as e:
    print('error during write:', type(e).__name__, str(e))
f.close()
with open('tmp.bin', 'rb') as f:
    data = f.read()
print('written bytes:', repr(data))
