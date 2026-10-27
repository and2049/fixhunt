class Mixin:
    def ping(self):
        return 'from Mixin'

class Base:
    def ping(self):
        return 'from Base'

class C(Mixin, Base):
    def ping(self):
        return super().ping()

c = C()
print(c.ping())
