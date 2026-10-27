import pathlib
def main():
    name = 'test'
    fmt = '{}.txt'.format
    val = 42
    # Multiple formatting styles used in path and content
    pathlib.Path(fmt('out')).write_text('%s %r' % (val, name))
    pathlib.Path(f'{name}_2.txt').write_text(str(val))
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
