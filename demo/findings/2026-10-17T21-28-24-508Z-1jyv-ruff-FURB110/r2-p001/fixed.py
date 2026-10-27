counter = [0]
def inc():
    counter[0] += 1
    return counter[0]
x = inc()
y = 99
z = x or y
print('side_effect_counter:', counter[0], 'z:', z)
