side = []

def log(msg):
    side.append(msg)
    return True

result = [log('A'), log('B')]
if not (not (result[0] and result[1])):
    side.append('taken')
print('side effects:', side)
