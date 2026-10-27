import os
template = 'Log: %(msg)s'
data = {'msg': 'hello', 'unused': open('tmp.txt', 'w')}
try:
    formatted = template % data
    with open('out.txt', 'w') as f:
        f.write(formatted)
    with open('out.txt') as f:
        print('File content:', repr(f.read()))
except Exception as e:
    print('Error:', type(e).__name__, str(e))
finally:
    if os.path.exists('tmp.txt'):
        os.remove('tmp.txt')
    if os.path.exists('out.txt'):
        os.remove('out.txt')
