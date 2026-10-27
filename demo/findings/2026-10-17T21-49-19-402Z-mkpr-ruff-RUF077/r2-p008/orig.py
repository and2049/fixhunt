a = 1
b = 2
class J:
    def m(self=a+b):
        a = 3
        b = 4
        return self
print(J().m())
