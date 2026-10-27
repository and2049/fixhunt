def a(): print('a called'); return 1
def b(): print('b called'); return 2
cond = False
print('Testing bin(a() if cond else b()).count(\'1\'):')
try:
    r = bin(a() if cond else b()).count('1')
except Exception as e:
    print(f'  Error: {type(e).__name__}: {e}')
cond = True
print('Testing bin(a() if cond else b()).count(\'1\'):')
try:
    r = bin(a() if cond else b()).count('1')
except Exception as e:
    print(f'  Error: {type(e).__name__}: {e}')
cond = False
print('Testing bin(a() if cond else b()).bit_count():')
try:
    r = bin(a() if cond else b()).bit_count()
except Exception as e:
    print(f'  Error: {type(e).__name__}: {e}')
cond = True
print('Testing bin(a() if cond else b()).bit_count():')
try:
    r = bin(a() if cond else b()).bit_count()
except Exception as e:
    print(f'  Error: {type(e).__name__}: {e}')
