ref = [0]

def get_dict():
    ref[0] += 1
    return {'a': ref[0], 'b': ref[0]*2}

print('Start ref:', ref[0])
for k, v in get_dict():  # Rule fires: get_dict called once per iteration? Actually once.
    print(f'{k}={v}', end=' ')
    ref[0] = 99  # Side effect in loop body
print()
print('Final ref:', ref[0])
