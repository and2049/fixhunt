from typing import Protocol

class P(Protocol):
    def f(self) -> None: ...

class Base:
    def f(self):
        return None

class Derived(Base):
    def f(self):
        return None

x: P = Derived()
print(type(x.f()))
