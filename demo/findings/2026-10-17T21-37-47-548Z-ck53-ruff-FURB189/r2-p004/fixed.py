class A(dict):  # comment on decl
    """doc"""
    x = 1
class B(list):  # another
    y = 2
print('A.x:', A.x)
print('B.y:', B.y)
print('A.__doc__:', A.__doc__)
print('B.__doc__:', B.__doc__)
