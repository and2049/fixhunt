def main():
    with open('tmp.txt', 'w') as f:
        f.write('0\n1\n2')
    with open('tmp.txt') as fp:
        for line in fp:
            if line.strip() == '1':
                fp.seek(0)
            print(line.strip())
    import os
    os.remove('tmp.txt')
if __name__ == '__main__':
    main()
