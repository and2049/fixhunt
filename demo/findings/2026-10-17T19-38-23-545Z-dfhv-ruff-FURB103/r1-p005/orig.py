import os
call_count = 0
def path():
    global call_count
    call_count += 1
    return 'p.txt'
with open(path(), 'w') as f:
    f.write(str(call_count))
with open('p.txt', 'r') as f:
    print(f.read())
print('path called:', call_count)
os.remove('p.txt')
