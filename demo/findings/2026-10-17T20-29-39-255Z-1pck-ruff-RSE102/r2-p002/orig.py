class Err:
    def __init__(self, v): self.v = v
    def __bool__(self): return self.v is not None
    def __len__(self): return 0 if self.v else 1

e = Err(None)
print('Before raise:', bool(e), len(e))
try:
    raise (e)()
except Err as caught:
    print('After catch:', bool(caught), len(caught))
