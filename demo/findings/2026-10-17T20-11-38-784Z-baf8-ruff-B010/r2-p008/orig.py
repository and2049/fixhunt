ref = []
def side_effect():
    ref.append('called')
    return 99

obj = type('Obj', (), {})()
result = setattr(obj, 'attr', side_effect() or 1)  # rule triggers
print('setattr result:', result, 'ref:', ref)
print('obj.attr:', obj.attr)

ref.clear()
obj2 = type('Obj', (), {})()
result2 = obj2.attr = side_effect() or 1  # rewritten
print('assignment result:', result2, 'ref:', ref)
print('obj2.attr:', obj2.attr)
print('Same side-effect timing?', len(ref) == 1 and ref[0] == 'called')
