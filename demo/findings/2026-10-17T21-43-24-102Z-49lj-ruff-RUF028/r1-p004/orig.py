# fmt: off
data = b'hello'
# fmt: on
try:
    print(data.upper())
except AttributeError as e:
    print(type(e).__name__, str(e))
