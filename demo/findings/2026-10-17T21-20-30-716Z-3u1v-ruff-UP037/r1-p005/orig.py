class Desc:
    def __get__(self, obj, owner):
        print('Desc accessed')
        return 42
class C:
    x: "Desc" = Desc()  # Rule may unquote -> triggers __get__ at class definition
print('C.x:', C.x)
