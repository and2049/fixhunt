def test():
    sep = '|'  # local override
    print('a', '', sep=sep)
    print('b')  # triggers FURB105
test()
