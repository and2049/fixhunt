def g():
    print('side effect')
    return 42
x = g()
if x in [g()]:  # Rule fires: [g()] → calls g() again → prints twice
    print('yes')
else:
    print('no')
