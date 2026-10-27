def make_func():
    exec('''
    def inner():
        if 0:
            pass
        else:
            pass  # structural
    ''')
    return inner
f = make_func()
f()
print('called')
