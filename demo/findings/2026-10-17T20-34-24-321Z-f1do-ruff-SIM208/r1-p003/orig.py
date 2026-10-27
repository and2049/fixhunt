counter = 0

def inc():
    global counter
    counter += 1
    print(f'inc called, counter={counter}')
    return counter > 0

if not (not inc()):
    print('branch taken')
print('final counter:', counter)
