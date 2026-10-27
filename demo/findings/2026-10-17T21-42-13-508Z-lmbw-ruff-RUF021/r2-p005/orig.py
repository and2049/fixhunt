def get_a():
    print('A evaluated')
    return True
def get_b():
    print('B evaluated')
    return False
def get_c():
    print('C evaluated')
    return True
res = get_a() or get_b() and get_c()
print('Result:', res)
