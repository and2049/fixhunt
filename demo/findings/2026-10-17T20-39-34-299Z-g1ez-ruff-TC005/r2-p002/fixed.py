import io, typing
buf = io.StringIO()
with buf:
    buf.write('hello')
print(buf.getvalue())
