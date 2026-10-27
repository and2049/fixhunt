def test():
    sep = '|'  # local override
    print('a', '', sep=sep)
    print('b', '', sep='')  # triggers FURB105
test()
