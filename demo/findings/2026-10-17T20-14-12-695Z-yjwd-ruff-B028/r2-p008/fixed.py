import warnings

x = [10]
def get_val():
    x[0] -= 1
    return x[0] / 2

warnings.warn(get_val(), category=RuntimeWarning)
print('x:', x)
