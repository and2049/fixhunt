import io
buf = io.StringIO()
with buf as f:  # noqa: UNKNOWN
    f.write('test')
print(buf.getvalue())
