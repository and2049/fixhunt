counter = 0
def gen():
    global counter
    counter += 1
    return [counter, counter*2]
print('First:', list(tuple(gen())))
print('Second:', list(tuple(gen())))
print(f'Counter: {counter}')
