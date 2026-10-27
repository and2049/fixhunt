def main():
    with open('tmp.txt', 'w') as f:
        f.write('0\n1\n2')
    with open('tmp.txt') as fp:
        for line in fp.readlines():
                fp.seek(0)
if __name__ == '__main__':
    main()
