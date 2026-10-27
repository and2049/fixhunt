def main():
    with open('tmp.txt', 'w') as f:
        f.write('x\ny\nz')
    with open('tmp.txt') as fp:
        for line in fp:
            if line.strip() == 'y':
                break
        print('last:', repr(line))
    import os
    os.remove('tmp.txt')
if __name__ == '__main__':
    main()
