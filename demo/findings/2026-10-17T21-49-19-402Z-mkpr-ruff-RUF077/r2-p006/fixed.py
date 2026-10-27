def gen():
    yield 1
    yield 2
class H:
    def m(self=gen()):
        try:
            return next(self)
        except StopIteration:
            return 0
print(H().m(), H().m())
