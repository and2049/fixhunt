import warnings

def f(lst=None):
    if lst is None:
        lst = []
    lst.append(99)
    return lst

lst = []
warnings.warn(str(f(lst)))
print('lst after:', lst)
