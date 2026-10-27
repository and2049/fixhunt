f = open('test.bin', 'wb')
if f is None:
  print('failed open')
else:
  print('opened ok')
try:
  f.write(b'hello')
  f.write(123)
except Exception as e:
  print('write error:', type(e).__name__, str(e))
finally:
  f.close()
import os
print('file size:', os.path.getsize('test.bin'))
os.remove('test.bin')
