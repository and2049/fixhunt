from decimal import Decimal

class IntDesc:
    def __get__(self, obj, owner):
        return f'desc:{self.value}'

class A:
    value = Decimal(str(5))  # Rule target
    desc = IntDesc()

print('Class access:', A.desc)
print('Instance access:', A().desc)
# After fix: value becomes Decimal(5), but desc still uses class.value via descriptor
# However, if value were used in desc, it would change -- here we show attr access depends on value type
print('A.value:', A.value, type(A.value))
