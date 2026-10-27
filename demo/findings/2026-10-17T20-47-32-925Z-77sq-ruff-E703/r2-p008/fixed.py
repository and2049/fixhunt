with open('test.bin', 'wb') as f:
  f.write(b'hello')  # Semicolon on write line
  f.truncate(2)
with open('test.bin', 'rb') as f:
  print(f.read())
import os
os.remove('test.bin')
