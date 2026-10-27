def f(): return True
def g(): return False
print(f'f()={f()} g()={g()}')
print(f'bin(f()).count(\'1\')={bin(f()).count(\'1\')} f().bit_count()={f().bit_count()}')
print(f'bin(g()).count(\'1\')={bin(g()).count(\'1\')} g().bit_count()={g().bit_count()}')
x = f()
y = g()
if bin(x).count('1') == x.bit_count(): print('Match for f()')
else: print('Mismatch for f()')
if bin(y).count('1') == y.bit_count(): print('Match for g()')
else: print('Mismatch for g()')
