class StdoutLike:
    def write(self, s): pass
out = StdoutLike()
if hasattr(out, 'write') or hasattr(out, 'flush'):
    out.write('hello')
print('done')
