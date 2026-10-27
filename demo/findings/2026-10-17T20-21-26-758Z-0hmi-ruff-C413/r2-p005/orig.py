counter = 0
def inc():
    global counter
    counter += 1
    return counter
x = [inc(), inc()]
r = list(sorted(x))
counter = 0
r2 = sorted(x)
print(r, counter)
print(r2, counter)
