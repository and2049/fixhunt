import pathlib
pathlib.Path('log.txt').write_text('first\n')
with open('log.txt', 'a') as f:
    f.write('second\n')
with open('log.txt', 'r') as f:
    print(f.read(), end='')
if os.path.exists('log.txt'):
    os.remove('log.txt')
