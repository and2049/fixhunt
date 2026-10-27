class C:
    def __init__(self, v): self.v = v
    def __bool__(self): return self.v > 0
    def __len__(self): return abs(self.v)
a = C(-1)
b = C(0)
c = C(1)
print(f'a_bool={bool(a)} a_len={len(a)} a_is_none={a is None}')
print(f'b_bool={bool(b)} b_len={len(b)} b_is_none={b is None}')
print(f'c_bool={bool(c)} c_len={len(c)} c_is_none={c is None}')
if bin(a).count('1'): print('a count True')
else: print('a count False')
if bin(b).count('1'): print('b count True')
else: print('b count False')
if bin(c).count('1'): print('c count True')
else: print('c count False')
