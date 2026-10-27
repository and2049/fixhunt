__all__ = ['helper']

def helper():
    return 'module_data'

def main():
    from module import *  # type: ignore
    with open('mod_out.txt', 'w') as f:
        f.write(helper())
    print(open('mod_out.txt').read())
    import os
    os.remove('mod_out.txt')

if __name__ == '__main__':
    main()
