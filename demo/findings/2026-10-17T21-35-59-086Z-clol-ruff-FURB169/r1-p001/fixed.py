counter = 0

def make_obj():
    global counter
    counter += 1
    return None

if make_obj() is None:
    print('before:', counter)
else:
    print('unreachable')
print('after:', counter)
