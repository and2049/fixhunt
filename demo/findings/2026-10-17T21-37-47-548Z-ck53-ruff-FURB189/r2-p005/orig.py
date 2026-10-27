import sys
class A(dict):
    pass
def check(obj):
    return isinstance(obj, dict) and type(obj) is dict  # strict built-in check
a = A()
print('isinstance(a, dict):', isinstance(a, dict))
print('check(a):', check(a))
print('type(a) is dict:', type(a) is dict)
