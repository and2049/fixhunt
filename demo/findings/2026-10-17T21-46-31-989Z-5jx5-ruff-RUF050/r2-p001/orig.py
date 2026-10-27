counter = [0]
def inc():
    counter[0] += 1
    return counter[0]
val = []
if inc() > 0:
    val.append(inc())  # Should append 2
print('inc calls:', counter[0], 'value:', val)
