from __future__ import annotations

class C:
    def m(cls) -> 'int':  # string annotation due to future import
        return 42
    m = classmethod(m)

print('C.m.__annotations__:', C.m.__annotations__)
print('C.m():', C.m())
