counter = 0
def getx():
    global counter
    counter += 1
    return counter
if getx() == 1 or getx() == 2:
    print('first or second call matched')
print('total calls:', counter)
