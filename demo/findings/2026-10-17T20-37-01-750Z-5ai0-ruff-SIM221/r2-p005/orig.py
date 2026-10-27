data = b'hello\nworld'
text = data.decode()
line_count = text.count('\n') or not text.count('\n')
print('lines:', line_count)
