from __future__ import annotations

class C:
    @classmethod
    def m(cls) -> 'int':  # string annotation due to future import
        return 42

print('C.m.__annotations__:', C.m.__annotations__)
print('C.m():', C.m())
