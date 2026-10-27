import warnings

args = ('dynamic message',)
warnings.warn(*args)
print('warning issued with *args')
