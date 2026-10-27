def func(x, *, y=1.0):  # y default is float
    return Decimal(x) + Decimal(y)
print(func(2))  # uses y=1.0 -> triggers on Decimal(y)
# After fix: Decimal(str(1.0)) -> Decimal('1.0')
# But note: default is evaluated once at definition, so replacement would be in the function's bytecode? 
# However, the fix would change the source: Decimal(y) -> Decimal(str(1.0)) only if y is a float literal, but y is a variable.
# Wait, the rule fires on Decimal(y) only if y is a float literal, which it's not.
# So this does not trigger. Need to adjust.
# Instead, make the call have a float literal in keyword argument:
print(func(2, y=1.0))  # now Decimal(1.0) in keyword argument -> triggers
