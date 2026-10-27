def main():
    with open('tmp.txt', 'w') as f:
        f.write('a\nb')
    with open('tmp.txt') as fp:
        for line in fp.readlines():
            if isinstance(fp.readlines(), list):
                print('is list')
if __name__ == '__main__':
    main()
