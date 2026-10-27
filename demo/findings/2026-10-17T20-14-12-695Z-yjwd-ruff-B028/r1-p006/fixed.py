import warnings
warnings.filterwarnings('ignore', lineno=15)
def inner():
    warnings.warn('filtered?')  # Line 15
inner()
print('No warning printed if filtered')
