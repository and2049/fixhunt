counter = 0
side_effects = []
def gen():
    global counter
    counter += 1
    side_effects.append(counter)
    return counter * 10
# Rule triggers on: not i in [10, 30, 50]
result = [i for i in map(gen, range(5)) if i not in [10, 30, 50]]
print('counter:', counter, 'side_effects:', side_effects, 'result:', result)
