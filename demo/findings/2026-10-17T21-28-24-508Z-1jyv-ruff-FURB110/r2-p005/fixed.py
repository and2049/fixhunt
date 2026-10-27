name = "Alice"
# Condition expression: f-string that evaluates to truthy
cond_expr = f'Hello {name}'
result = cond_expr or 'unnamed'
print('result:', result)
# Original: evaluates f-string once
# Fixed: cond_expr or 'unnamed' -> evaluates once, same
# No side effect, so behavior same. Not good.
# Need condition with side effect in formatting.
# Redo.
