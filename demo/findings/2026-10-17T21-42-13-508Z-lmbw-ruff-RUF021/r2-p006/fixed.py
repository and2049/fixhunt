def get_d():
    print('D evaluated')
    return False
def get_e():
    print('E evaluated')
    return True
def get_f():
    print('F evaluated')
    return False
res = (get_d() and get_e()) or get_f()
print('Result:', res)
