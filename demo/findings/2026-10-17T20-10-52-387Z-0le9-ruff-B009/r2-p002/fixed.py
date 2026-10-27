d = {}
d['s'] = 'normalized_value'
setattr(type('Obj', (), {}), '\u017f', 'long_s_value')  # dynamically add attr
obj = type('Obj', (), {'s': 'normalized_value', '\u017f': 'long_s_value'})()
val1 = getattr(obj, '\u017f')  # should be 'long_s_value'
val2 = d.get('\u017f', 'missing')  # key '\u017f' not in d, but 's' is
print(f'getattr: {val1}, dict.get: {val2}')
# After fix: obj.\u017f -> obj.s -> 'normalized_value', breaking equivalence
