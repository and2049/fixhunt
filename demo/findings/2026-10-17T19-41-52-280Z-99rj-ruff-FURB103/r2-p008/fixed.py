import pathlib
__all__ = ['helper']

def helper():
    return 'module_data'

def main():
    from module import *  # type: ignore
    pathlib.Path('mod_out.txt').write_text(helper())
    print(open('mod_out.txt').read())
    import os
    os.remove('mod_out.txt')

if __name__ == '__main__':
    main()
