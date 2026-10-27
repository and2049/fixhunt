a = None
b = False
result = type(a) is type(None) and b
print('Result of type(a) is type(None) and b:', result)
# After fix: a is None and b -> evaluates to False
# But we want to see if the fix changes grouping
result2 = (type(a) is type(None)) and b
print('With explicit parens:', result2)
