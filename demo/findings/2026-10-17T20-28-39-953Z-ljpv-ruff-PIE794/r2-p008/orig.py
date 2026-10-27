class Parent:
    attr = 'parent'
class Child(Parent):
    attr = 'child'
    attr = 'overridden'
print(Child.attr)
