def write_and_return(f):
    f.write('test')
    return f
with open('tmp.txt', 'w') as f:
    f2 = write_and_return(f)
    print(f2.write(' more'))
with open('tmp.txt', 'r') as f:
    print(f.read())
if os.path.exists('tmp.txt'):
    os.remove('tmp.txt')
