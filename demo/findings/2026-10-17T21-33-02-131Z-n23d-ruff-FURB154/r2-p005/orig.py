def f(lst=[]):
    global a
    global b
    lst.append(a)
    lst.append(b)
    return lst
a = 10
b = 20
print(f())
print(f())
