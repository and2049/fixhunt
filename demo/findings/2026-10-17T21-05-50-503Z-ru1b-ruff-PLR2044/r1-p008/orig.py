def f(x, lst=[]):  # 
    lst.append(x)
    return lst
print(f(1))
print(f(2))
# Reset and show correct
f.__defaults__ = ([],)
print(f(1))
print(f(2))
