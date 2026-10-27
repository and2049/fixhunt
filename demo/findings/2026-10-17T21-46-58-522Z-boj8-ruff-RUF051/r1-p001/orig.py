def get_dict():
    global counter
    counter += 1
    return {'a': 1}
counter = 0
d = get_dict()
if 'a' in get_dict():  # Rule triggers here
    del get_dict()['a']
print('counter:', counter)
