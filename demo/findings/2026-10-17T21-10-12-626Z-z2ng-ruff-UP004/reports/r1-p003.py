class Mixin:
    def ping(self):
        return 'from Mixin'
class Base:
    def ping(self):
        return 'from Base'
class C(object, Mixin, Base):
    def ping(self):
        return super().ping()
