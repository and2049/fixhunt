def make_dict(seq=[(i, i*2) for i in range(3)]):
    return dict(seq)
def make_dict_fixed():
    return {(k, v) for k, v in [(i, i*2) for i in range(3)]}
print('make_dict():', make_dict())
print('make_dict_fixed():', make_dict_fixed())
# Now rebind the default
seq = [(0, 0), (1, 1), (2, 2)]
print('make_dict() after rebind:', make_dict())
