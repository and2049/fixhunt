import io
buf = io.BytesIO()
buf.write(b'super\nline2')
buf.seek(0)
line = buf.readline()  # b'super\n'
if line.startswith(b'super'):
    try:
        line.super.decode()  # triggers PLW0245 -> line.super().decode()
    except AttributeError as e:
        print(f'AttributeError: {e}')
else:
    print('no match')
