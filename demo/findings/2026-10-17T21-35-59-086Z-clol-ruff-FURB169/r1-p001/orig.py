counter = 0

def make_obj():
    global counter
    counter += 1
    return None

if type(make_obj()) is type(None):
    print('before:', counter)
else:
    print('unreachable')
print('after:', counter)
