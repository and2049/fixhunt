def append_join(x, lst=[]):
    lst.append(x)
    return '-'.join((lst[0], lst[-1]))
print(append_join(1))  # ['1'] -> '1-1'
print(append_join(2))  # ['1', '2'] -> '1-2'
# After f-string fix: f'{lst[0]}-{lst[-1]}' still uses current list, so same?
