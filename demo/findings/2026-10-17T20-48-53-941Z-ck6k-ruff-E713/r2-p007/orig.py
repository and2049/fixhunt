counter = 0
def make_list():
    global counter
    counter += 1
    return [counter]
print(not 1 in make_list()))  # triggers; make_list() called once
print('counter:', counter)
counter = 0
print(1 not in make_list()))  # after fix equivalent
print('counter:', counter)
