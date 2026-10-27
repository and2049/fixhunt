x = 'hidden'
def test():
    x = 'local'
    return str(x)
print(test())
exec('print(str(x))')  # uses global x
