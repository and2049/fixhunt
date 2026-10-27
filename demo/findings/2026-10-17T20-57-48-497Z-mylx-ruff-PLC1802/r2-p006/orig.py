counter = 0
def get_list():
    global counter
    counter += 1
    return [1] * counter

if len(get_list()) > 0:
    print('first:', counter)
if len(get_list()) > 0:
    print('second:', counter)
