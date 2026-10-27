import typing
T = int
class C:
    def m(self=T):
        if isinstance(self, int):
            return 1
        return 0
print(C().m())
