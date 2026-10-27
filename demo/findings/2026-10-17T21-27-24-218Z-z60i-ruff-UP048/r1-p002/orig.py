from decimal import Decimal, getcontext
getcontext().prec = 6
vals = []
i = 0
while 1:
    if i == 3:
        break
    f = float(i) / 2
    d = Decimal(str(f))
    vals.append((f, d))
    i += 1
print(vals)
