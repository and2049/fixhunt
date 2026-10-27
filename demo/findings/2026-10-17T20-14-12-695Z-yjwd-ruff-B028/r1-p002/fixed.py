import warnings
original_warn = warnings.warn
def patched_warn(message, *, category=None):
    print(f'Patched warn called with: {message}, category={category}')
    return None
warnings.warn = patched_warn
try:
    warnings.warn('test')
except TypeError as e:
    print(f'TypeError: {e}')
