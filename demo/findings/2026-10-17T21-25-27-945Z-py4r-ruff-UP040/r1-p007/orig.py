name = 'world'
F = TypeAliasType('F', f'Hello {name}')
print('F is:', F)
# After fix: `type F = f'Hello {name}'` evaluates f-string at definition time
# If name changes later, alias doesn't update
name = 'there'
print('After name change, F still:', F)
try:
    # F is a string literal in fix, so no dynamic behavior
    pass
except:
    pass
print('Name is now:', name)
