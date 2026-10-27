def f(x, lst=[]):
    lst.append(x)
    return lst
data = [3, 1, 2]
sorted_data = sorted(data, key=f)
list_wrapped = list(sorted_data)
print('Default arg state after key calls:', f.__defaults__[0])
print('Wrapped list:', list_wrapped)
