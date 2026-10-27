def f():
    none = 5
    return none is None
print(f())  # Prints False before fix; after fix, becomes `none == None` → raises NameError because `None` is overwritten as local var
