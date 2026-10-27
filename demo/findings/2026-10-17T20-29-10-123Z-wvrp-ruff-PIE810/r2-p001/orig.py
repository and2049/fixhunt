data = b'\r\nhello\n'
if data.endswith(b'\n') or data.endswith(b'\r\n'):
    print('line ends:', data[-2:])
else:
    print('no match')
