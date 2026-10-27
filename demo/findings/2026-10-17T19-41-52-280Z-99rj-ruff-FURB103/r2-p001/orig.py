def main():
    name = 'test'
    fmt = '{}.txt'.format
    val = 42
    # Multiple formatting styles used in path and content
    with open(fmt('out'), 'w') as f:
        f.write('%s %r' % (val, name))
    with open(f'{name}_2.txt', 'w') as f:
        f.write(str(val))
    # Verify outputs
    import os
    print(open('test.out').read().strip())
    print(open('test_2.txt').read().strip())
    try:
        os.remove('test.out')
        os.remove('test_2.txt')
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    main()
