from typing import TypeAlias
MyBytes: TypeAlias = bytes
def g(b: MyBytes) -> str:
    return b.decode('utf-8')
try:
    print(g(b'hello\n'))
except Exception as e:
    print(type(e).__name__, e)
