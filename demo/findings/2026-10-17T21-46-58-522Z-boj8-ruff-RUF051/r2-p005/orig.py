counter = 0
def next_key():
    global counter
    counter += 1
    return str(counter)
store = {}
if next_key() in store:
    del store[next_key()]
print('counter after if-del:', counter)
counter = 0
store = {}
if next_key() in store:
    del store[next_key()]
print('counter after if-del (second):', counter)
