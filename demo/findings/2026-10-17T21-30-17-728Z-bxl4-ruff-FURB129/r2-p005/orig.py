def main():
    with open('tmp.txt', 'w') as f:
        f.write('a\nb')
    with open('tmp.txt') as fp:
        lines = fp.readlines()
        def gen():
            for l in lines:
                yield l
        g = gen()
        next(g)
        for line in g:
            print(line.strip())
    import os
    os.remove('tmp.txt')
if __name__ == '__main__':
    main()
