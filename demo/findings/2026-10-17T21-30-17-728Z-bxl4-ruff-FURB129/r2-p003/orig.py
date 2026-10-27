def main():
    with open('tmp.txt', 'w') as f:
        f.write('aa\nbb\ncc\ndd')
    with open('tmp.txt') as fp:
        for chunk in fp.readlines(5):
            print(repr(chunk))
    import os
    os.remove('tmp.txt')
if __name__ == '__main__':
    main()
