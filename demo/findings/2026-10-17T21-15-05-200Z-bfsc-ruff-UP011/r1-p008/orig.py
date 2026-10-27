import functools
@functools.lru_cache()
def read_file(path):
  with open(path, 'r', encoding='utf-8') as f:
    return f.read()
with open('test.txt', 'w', encoding='utf-8') as f:
  f.write('hello')
print(read_file('test.txt'))
import os
os.remove('test.txt')
