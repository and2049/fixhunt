def f(x, y=[]):
    try:
        if not y:
            raise ValueError('empty')
    except ValueError as e:
        y.append(x)
        return y
    return y

print(f(1))
print(f(2))
print(f(3))  # Default list accumulates across calls
