def get_data():
    print('get_data called')
    return 'content'

def main():
    with open('test.txt', 'w') as f:
        f.write(get_data())
    print(open('test.txt').read())
    import os
    os.remove('test.txt')

if __name__ == '__main__':
    main()
