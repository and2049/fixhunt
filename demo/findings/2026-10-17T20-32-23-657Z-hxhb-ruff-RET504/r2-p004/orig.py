def f():
    data = [1, 2, 3]
    result = [(x := i) * 2 for i in data if x > 0]
    return result
print(f())
