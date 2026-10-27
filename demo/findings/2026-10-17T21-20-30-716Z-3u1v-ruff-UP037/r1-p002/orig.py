class A: pass
f = lambda: "A"  # Rule may unquote to lambda: A
try:
    print('lambda result:', f())
except Exception as e:
    print(type(e).__name__, ':', e)
