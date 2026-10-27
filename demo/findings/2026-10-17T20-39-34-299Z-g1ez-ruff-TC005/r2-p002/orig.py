import io, typing
buf = io.StringIO()
with buf:
    if typing.TYPE_CHECKING:
        pass
    buf.write('hello')
print(buf.getvalue())
