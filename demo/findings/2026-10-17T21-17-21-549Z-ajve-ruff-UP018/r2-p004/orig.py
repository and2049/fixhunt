i = 0
def inc():
    global i
    i += 1
    return i
vals = [str(inc()), str(inc())]
print('vals:', vals, 'i:', i)
