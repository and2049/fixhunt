def make_func():
    return = 42  # shadows built-in
    def inner():
        if True:
            return return
        return None
    return inner
f = make_func()
del return  # remove shadow
print(f())
