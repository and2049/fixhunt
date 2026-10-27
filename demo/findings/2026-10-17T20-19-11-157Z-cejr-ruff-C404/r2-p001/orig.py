def f():
    # This comment should stay
    d = dict([
        (x, x*2)  # inline
        for x in [1,2]  # loop comment
    ])
    return len(d)
