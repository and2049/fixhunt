counter = 0
def inc():
    global counter
    counter += 1
    return counter
s = '{inc()} {inc()}'
print('Before fix:', s.format(inc=inc))
print('After fix :', eval('f"' + s[1:-1] + '"'))
