counter = [0]
def inc():
    counter[0] += 1
    return counter[0]
d = dict((i, inc()) for i in range(3))
print('dict result:', d)
print('counter:', counter[0])
counter[0] = 0
d2 = {i: inc() for i in range(3)}
print('comp result:', d2)
print('counter after comp:', counter[0])
