def get_flag():
    print('get_flag called')
    return False
result = assert False or get_flag()
print('result:', result)
