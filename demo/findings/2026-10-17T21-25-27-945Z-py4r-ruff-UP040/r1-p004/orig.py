class Desc:
    def __get__(self, obj, owner):
        return 'desc'
C = TypeAliasType('C', Desc)
class A:
    attr = C
print(A().attr)
print(type(A.attr))
# After fix: `type C = Desc` makes C a type, not Desc instance; attr becomes class var of type Desc
# But descriptor protocol only works on instances; A.attr is now a type, not descriptor
# So A().attr raises AttributeError (no __get__ on type)
try:
    print(A().attr)
except AttributeError as e:
    print('Attr error:', e)
