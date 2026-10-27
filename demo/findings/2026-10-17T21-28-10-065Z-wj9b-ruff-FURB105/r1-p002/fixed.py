import io
buf = io.BytesIO()
try:
    print(b''.decode(), file=buf)
except Exception as e:
    print(type(e).__name__, str(e))
else:
    print(buf.getvalue())
buf.close()
