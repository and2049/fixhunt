a = []
b = []
if a == []:
  print('a is new list')
else:
  print('a is not new list')
if a == []:
  print('a is empty')
else:
  print('a is not empty')
cache = []
def get_cache():
  return cache
x = get_cache()
if x == []:
  print('cache hit')
else:
  print('cache miss')
