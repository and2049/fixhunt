from typing import TYPE_CHECKING, TypeAlias
import io
if TYPE_CHECKING:
    StringWriter = io.StringIO
Log: TypeAlias = StringWriter
try:
    with Log() as f:
        f.write('test')
        print('written:', f.getvalue())
except Exception as e:
    print(type(e).__name__, e)
