def f():
    if True:
        x = 1
        pass  # Rule triggers: removable pass
        # y = 2  # This comment must stay; if dedented, it becomes top-level
    print('x:', x)
f()
