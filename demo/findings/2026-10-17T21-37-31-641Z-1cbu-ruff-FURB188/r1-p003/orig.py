class C:
    def __len__(self): return 0
    def startswith(self, _): return True
    def endswith(self, _): return False
c = C()
try:
    if c.startswith('pre'):
        c = c[:-3] if c.startswith('pre') else c
    print(len(c))
except Exception as e:
    print(f'{type(e).__name__}: {e}')
