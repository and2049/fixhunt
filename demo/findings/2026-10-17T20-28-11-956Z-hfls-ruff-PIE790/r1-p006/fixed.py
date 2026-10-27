def f():
    if True:
        x = 1
        # Rule triggers: removable pass
        # y = 2  # This comment must stay; if dedented, it becomes top-level
    print('x:', x)
f()
