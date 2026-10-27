foo = [1]
bar = foo  # alias
foo = foo + [2]  # new list
print('plain:', foo, bar, id(foo), id(bar))
foo2 = [1]
bar2 = foo2
foo2 += [2]  # mutates in-place
print('aug:', foo2, bar2, id(foo2), id(bar2))
