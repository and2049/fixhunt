def f(lst=None):
    if lst is None: lst = []
    lst = lst + [1]  # Trigger
    return lst
print(f())
print(f())
# After fix: lst += [1] makes default [] mutable across calls
