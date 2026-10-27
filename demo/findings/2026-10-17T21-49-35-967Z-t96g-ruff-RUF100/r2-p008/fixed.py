import io
buf = io.StringIO()
with buf as s:
    s.write('hello')
print(buf.getvalue())
