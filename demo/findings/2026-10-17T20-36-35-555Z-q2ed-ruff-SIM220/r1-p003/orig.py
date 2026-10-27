def f():
    return True
if f() and not f():  # annotation-like use
    pass
try:
    x
except NameError as e:
    print('NameError:', e)
else:
    print('x defined:', x)
