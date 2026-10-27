f = open('test.txt', 'w')
data = {'msg': 'hello', 'junk': 123}  # junk unused
try:
    f.write('%(msg)s\n' % data)
except Exception as e:
    print('Write error:', type(e).__name__, str(e))
f.close()
with open('test.txt', 'r') as f:
    print('File content:', repr(f.read()))
