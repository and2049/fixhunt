def outer():
    x = 1
    s = {1, 2}
    def inner():
        x = 2  # shadows outer x
        if x in s:  # refers to inner x=2
            s.remove(x)  # removes 2
    inner()
    print('Set after inner:', s)
    print('Outer x:', x)
outer()
