seq = []
def log(v): seq.append(v); return v

class A:
    x = log(1)
    y = log(2)

print(seq)
print(A.x, A.y)
del A
