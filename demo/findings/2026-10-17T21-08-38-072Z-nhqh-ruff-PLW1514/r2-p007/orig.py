import os

with open('bad.txt', 'w') as f:
    f.write('broken')

try:
    f = open('bad.txt')  # rule fires: adds encoding='utf-8'
    try:
        raise ValueError('fail')
    finally:
        f.close()
        print('Finally ran')
except ValueError as e:
    print('Caught:', e)
except Exception as e:
    print('Other:', type(e).__name__, e)

try:
    with open('bad.txt') as f:
        raise ValueError('fail')
except ValueError as e:
    print('With-stmt caught:', e)

os.remove('bad.txt')
