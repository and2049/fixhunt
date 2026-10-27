data_b = b'hello\nworld'
data_s = 'hello\nworld'
print('bytes lines:', len(data_b.splitlines()))
print('str lines:', len(data_s.splitlines()))
if type(data_b) is type(None):
    print('bytes is None')
else:
    print('bytes is not None')
