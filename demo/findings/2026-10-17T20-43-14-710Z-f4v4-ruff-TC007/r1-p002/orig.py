from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    class Base:
        pass
A: TypeAlias = Base
try:
    class C(A):  # This line triggers TC007
        pass
    print('Success:', C.__bases__)
except Exception as e:
    print(type(e).__name__, e)
