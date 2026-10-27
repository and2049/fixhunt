import warnings

def wrapper(*args):
    warnings.warn(*args)

wrapper('test', category=DeprecationWarning)
print('warning issued')
