import abc
log = []
def writer():
  log.append('write')
  return type('W', (), {'write': writer, '__enter__': lambda s: None, '__exit__': lambda s, *a: None})()
with writer() as w:
  w.write()
print(log)
