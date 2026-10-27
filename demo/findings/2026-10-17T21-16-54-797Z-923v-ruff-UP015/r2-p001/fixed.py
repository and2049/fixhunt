def main():
    path = 'data.txt'
    # Use % formatting: relies on exact string 'r' being present
    cmd = "open('%s', 'r')" % path
    exec(cmd)
    f = open(path)
    f.write('hello\n')
    f.close()
    f = open(path)
    print(f.read().strip())
    f.close()
    import os
    os.remove(path)
if __name__ == '__main__':
    main()
