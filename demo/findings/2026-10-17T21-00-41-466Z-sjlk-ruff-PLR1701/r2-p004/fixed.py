def f(): return 0
def g(): return 1
result = f() or isinstance(0, int) or isinstance(0, str)
print(result)
