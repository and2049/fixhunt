def f(): return 1
x = 'abc'
try:
    if x.startswith('a') or x.startswith(f()):
        print('yes')
except Exception as e:
    print(type(e).__name__, e)
