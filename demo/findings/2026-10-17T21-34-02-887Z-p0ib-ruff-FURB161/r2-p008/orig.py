import os
open('test.txt', 'w').write('hello')
try:
    p_len = len('test.txt')
    print(f'Path length: {p_len}')
    print(f'bin(len(\'test.txt\')).count(\'1\') = {bin(p_len).count(\'1\')}')
    print(f'bin(len(\'test.txt\')).bit_count() = {p_len.bit_count()}')
    os.symlink('test.txt', 'link.txt')
    l_len = len(os.readlink('link.txt'))
    print(f'Symlink target length: {l_len}')
    print(f'bin(len(os.readlink(\'link.txt\'))).count(\'1\') = {bin(l_len).count(\'1\')}')
    print(f'bin(len(os.readlink(\'link.txt\'))).bit_count() = {l_len.bit_count()}')
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}')
finally:
    try:
        os.unlink('test.txt')
        os.unlink('link.txt')
    except FileNotFoundError:
        pass
