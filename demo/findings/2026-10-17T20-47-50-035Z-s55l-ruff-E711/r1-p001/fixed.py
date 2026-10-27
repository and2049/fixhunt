def f(a=[]):
    if a == None:
        a = [1]
    a.append(2)
    print(a)
f()
f()
f()
