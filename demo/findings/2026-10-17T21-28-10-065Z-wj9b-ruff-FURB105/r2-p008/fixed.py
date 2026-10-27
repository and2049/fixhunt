i = 0
def inc():
    global i
    i += 1
    return i
print('', sep=inc(), end='')
print(f' i={i}')
