counter = 0

def side_effect():
    global counter
    counter += 1
    return str(counter)

def main():
    global counter
    counter = 0
    # Path expression with side effect
    with open(side_effect() + '.txt', 'w') as f:
        f.write(side_effect())
    print('counter:', counter)
    print(open('12.txt').read())
    import os
    os.remove('12.txt')

if __name__ == '__main__':
    main()
