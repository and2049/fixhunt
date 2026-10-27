ref = [0]
def side():
    ref[0] += 1
    return ref[0]
d = {}
# Expression with side effect in default position
val = d.get('missing', side())
print('val:', val, 'ref:', ref[0])
# Second call shows accumulated effect
val2 = d.get('missing', side())
print('val2:', val2, 'ref:', ref[0])
