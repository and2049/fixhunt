a = [1, 2, 3]
b = [4, 5]  # unequal length
def func(x=list(zip(a, b, strict=True))):  # fixed version would evaluate here
    return x

print('About to call func')
try:
    print(func())  # Would have raised at definition if fixed, but not now
except Exception as e:
    print(type(e).__name__, str(e))
print('a=', a, 'b=', b)
