counter = 0
def gen():
    global counter
    counter += 1
    yield (counter, counter*10)
for i in range(2):
    d = {k: v for k, v in gen()}
    print('round', i, 'dict:', d, 'counter:', counter)
