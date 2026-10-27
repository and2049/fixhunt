def g():
    print('g called')
    return 5
def h():
    print('h called')
    return 3
cond = False
try:
    v = bin(g() if cond else h()).count('1')
except: pass
print('g' if not cond else 'h', 'not called' if cond else 'called')
cond = True
try:
    v = bin(g() if cond else h()).count('1')
except: pass
print('g' if cond else 'h', 'called' if cond else 'not called')
