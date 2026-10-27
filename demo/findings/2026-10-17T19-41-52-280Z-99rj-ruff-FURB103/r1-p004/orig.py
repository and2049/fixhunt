with open('test.txt', 'w+') as f:
    f.write('hello')
    f.seek(0)
    content = f.read()
    print(f'Read back: {content}')
import nos
os.remove('test.txt')
