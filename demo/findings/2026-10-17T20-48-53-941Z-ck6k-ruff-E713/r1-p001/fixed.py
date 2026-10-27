def outer():
    xs = []
    ys = []
    # Rule triggers on: not (val := x) in xs
    f = lambda: [(ys.append(val), val)[1] for x in range(3) if (val := x) not in xs]
    xs.extend([0, 2])
    result = f()
    print('ys:', ys, 'result:', result)
outer()
