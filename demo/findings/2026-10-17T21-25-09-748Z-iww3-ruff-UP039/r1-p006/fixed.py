import pathlib
class A:
    p = pathlib.Path('tmp.txt')
    p.write_text('hi')
print('exists:', A.p.exists())
print('content:', A.p.read_text())
A.p.unlink()
