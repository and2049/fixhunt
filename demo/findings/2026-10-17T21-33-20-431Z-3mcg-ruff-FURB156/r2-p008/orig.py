side = []
def get_digit_str():
    side.append('called')
    return '0123456789'
if '5' in get_digit_str():
    print('side effect log:', side)
