def f(a, b): return a + b.decode()
s1 = b'hello'
s2 = ['world', '!']
try:
    res = list(map(f, s1, s2))
except Exception as e:
    print('error:', type(e).__name__, str(e))
else:
    print('result:', ''.join(res))
