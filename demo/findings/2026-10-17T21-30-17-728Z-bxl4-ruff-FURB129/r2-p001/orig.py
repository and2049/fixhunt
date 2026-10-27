def main():
    with open('tmp.txt', 'w') as f:
        f.write('a\nb\nc')
    with open('tmp.txt') as fp:
        for line in fp.readlines():
            s = f'Line: {line!r}'
            print(s)
    import os
    os.remove('tmp.txt')
if __name__ == '__main__':
    main()
