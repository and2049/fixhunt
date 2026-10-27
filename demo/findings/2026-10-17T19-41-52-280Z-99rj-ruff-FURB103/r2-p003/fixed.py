import pathlib
def get_data():
    print('get_data called')
    return 'content'

def main():
    pathlib.Path('test.txt').write_text(get_data())
    print(open('test.txt').read())
    import os
    os.remove('test.txt')

if __name__ == '__main__':
    main()
