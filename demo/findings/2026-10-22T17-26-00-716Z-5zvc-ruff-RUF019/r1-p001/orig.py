d = {'\n': b'ok', '\r\n': b'bad'}
data = {b'\n': True, b'\r\n': False}
for k, v in list(d.items()) + list(data.items()):
    if isinstance(k, str) and k in d and d[k]:
        print('str:', repr(d[k]))
    elif isinstance(k, bytes) and k in data and data[k]:
        print('bytes:', repr(data[k]))
