ref = []
def f():
    ref.append(1)
    return ref
x = f()
if x is not f():
    print('different call')
else:
    print('same call')
print('ref:', ref)
