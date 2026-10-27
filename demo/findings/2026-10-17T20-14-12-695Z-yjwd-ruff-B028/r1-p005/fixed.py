import warnings
def log_warn(msg, stack=[]):
    stack.append(msg)
    warnings.warn(msg)
    return stack
log_warn('first')
log_warn('second')
print(f'Stack after two warns: {log_warn([])}')
