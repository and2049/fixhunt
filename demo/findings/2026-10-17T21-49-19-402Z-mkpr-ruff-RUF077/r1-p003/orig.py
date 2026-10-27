class Base:
    def handle(self='base'):
        return f'Base: {self}'

class Sub(Base):
    def handle(self):
        return super().handle() + ' -> Sub'

b = Base()
s = Sub()
print(b.handle())
print(s.handle())
