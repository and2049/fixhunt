from builtins import str

x = str(input := '42') or 0
print(x, input)
