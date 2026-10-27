import pathlib
counter = 0

def side_effect():
    global counter
    counter += 1
    return str(counter)

def main():
    global counter
    counter = 0
    # Path expression with side effect
    pathlib.Path(side_effect() + '.txt').write_text(side_effect())
    print('counter:', counter)
    print(open('12.txt').read())
    import os
    os.remove('12.txt')

if __name__ == '__main__':
    main()
