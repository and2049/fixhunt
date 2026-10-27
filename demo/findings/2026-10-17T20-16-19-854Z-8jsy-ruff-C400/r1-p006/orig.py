side = []
def get_data():
    side.append('get_data')
    return [1, 2]
result = list(x + 1 for x in get_data())
print('side:', side)
print('result:', result)
