counter = 0

def make_dict():
    global counter
    counter += 1
    return {'a': 1, 'b': 2}

print('Before loop:', counter)
for k, v in make_dict():  # Rule fires here: unpacking dict without .items()
    print(f'{k}:{v}', end=' ')
print()
print('After loop:', counter)
