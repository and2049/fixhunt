def f(s, lst=[]):
    lst.append(int(s[2:], 2))
    return lst
print(f('0b1'))
print(f('0b10'))
