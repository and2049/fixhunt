counter = 0
def next_int():
    global counter
    counter += 1
    return counter
a = next_int()
b = next_int()
if isinstance(a, int) or isinstance(b, str):
    print('taken')
else:
    print('not taken')
print(f'counter={counter}')
