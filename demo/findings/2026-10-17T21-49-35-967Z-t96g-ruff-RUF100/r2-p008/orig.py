import io
buf = io.StringIO()
with buf as s:
    s.write('hello')  # noqa: SIM115
print(buf.getvalue())
