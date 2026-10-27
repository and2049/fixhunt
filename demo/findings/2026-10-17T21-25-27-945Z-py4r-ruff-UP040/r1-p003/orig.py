B = TypeAliasType('WrongName', int)
print(B)
print(type(B))
# After fix: `type WrongName = int` creates name 'WrongName', but var 'B' remains unbound to it
# So B is still the TypeAliasType object, not the alias; referencing WrongName fails
try:
    print(WrongName)
except NameError as e:
    print('Missing:', e)
