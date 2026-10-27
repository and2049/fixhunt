import typing
j = 7
k = typing.cast(list[int], [j])  # This is a list of one int
print(k[0] + 1)
