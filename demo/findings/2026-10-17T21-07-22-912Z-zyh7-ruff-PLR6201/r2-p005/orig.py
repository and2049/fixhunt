def f(x, lst=[1, 2]):
    return x in lst
print(f(1))  # True
print(f(3))  # False
lst = [1, 2]
print(f(1, lst))  # True
lst.append(3)
print(f(3, lst))  # True - original list mutated
