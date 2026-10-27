import string
side = []
def get_digit_str():
    side.append('called')
    return string.digits
if '5' in get_digit_str():
    print('side effect log:', side)
