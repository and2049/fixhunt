"""Module doc"""
x = 'abc'
# need prefix
def check():
    if x.startswith('a')  # first
       or x.startswith('ab'):  # second
        return True
    return False
print(check())
