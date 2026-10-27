import os
os.remove('test.txt') if os.path.exists('test.txt') else None
with open('test.txt', 'w') as f:
    f.write('10\n3\n5')
with open('test.txt', 'r') as fp:
    total = 0
    count = 0
    for num in fp:
        n = int(num.strip())
        total += n
        count += 1
        avg = total / count
        print(f'Running avg: {avg:.2f}')
print('Final average:', total / count if count else 0)
os.remove('test.txt')
