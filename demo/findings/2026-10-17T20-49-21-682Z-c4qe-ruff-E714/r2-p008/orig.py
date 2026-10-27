ref = []
def f():
    ref.append(1)
    return ref
x = f()
if not x is f():
    print('different call')
else:
    print('same call')
print('ref:', ref)
