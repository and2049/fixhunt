l = []
def side_effect():
    l.append(1)
    return {'a': 1}
d = side_effect()
if 'a' in side_effect():  # side_effect called twice
    del side_effect()['a']  # and again
print('side_effect calls:', len(l))
