counter = [0]
def inc():
    counter[0] += 1
    return counter[0]
x = inc()
y = inc() or not inc()
print('left:', x, 'middle:', y)
