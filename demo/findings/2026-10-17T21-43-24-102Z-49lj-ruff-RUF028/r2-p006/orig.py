# fmt: off
i = 0
def next_i():
    nonlocal i
    i += 1
    return i
a = [next_i(), next_i()]
print(a)
