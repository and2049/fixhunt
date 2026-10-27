string = 'overridden'
try:
    print(string.upper())
except AttributeError as e:
    print('Error:', e)
# After fix: import string would shadow local var, but we simulate risk by showing what happens if name clashes
