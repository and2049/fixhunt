class A:
    x = 5
class B(A):
    def get(self):
        return super().x
obj = B()
print(bin(obj.get()).count('1'))
obj2 = type('Obj', (), {'x': 10})()
print(bin(obj2.x).count('1'))
