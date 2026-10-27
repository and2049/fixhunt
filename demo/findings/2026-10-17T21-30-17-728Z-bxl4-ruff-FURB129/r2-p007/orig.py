def main():
    with open('tmp.txt', 'w') as f:
        f.write('start\nend')
    with open('tmp.txt') as fp:
        i = 0
        for line in fp.readlines():
            print(f'{i}: {line.strip()}')
            i += 1
    import os
    os.remove('tmp.txt')
if __name__ == '__main__':
    main()
