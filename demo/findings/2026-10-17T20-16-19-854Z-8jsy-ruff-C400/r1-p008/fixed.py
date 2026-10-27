lines = [b'hello\n', b'world\n']
try:
    decoded = list(line.decode('utf-8').strip() for line in lines)
except UnicodeDecodeError as e:
    print('UnicodeDecodeError:', e)
else:
    print('decoded:', decoded)
