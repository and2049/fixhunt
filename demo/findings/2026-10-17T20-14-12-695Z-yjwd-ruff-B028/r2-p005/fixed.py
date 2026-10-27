import warnings

def inner():
    warnings.warn('alert')

def outer():
    inner()

outer()
