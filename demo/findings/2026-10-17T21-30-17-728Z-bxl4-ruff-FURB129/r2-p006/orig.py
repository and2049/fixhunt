def main():
    with open('tmp.txt', 'w') as f:
        f.write('1\n2')
    with open('tmp.txt') as fp:
        for x in (fp.readlines(),):
            for line in x:
                print(line.strip())
    import os
    os.remove('tmp.txt')
if __name__ == '__main__':
    main()
