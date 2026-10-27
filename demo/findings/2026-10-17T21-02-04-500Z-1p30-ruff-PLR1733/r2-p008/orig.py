import sys
sys.__dict__['PLUGIN_VALUE'] = 100
for k, v in sys.__dict__.items():
    if k == 'PLUGIN_VALUE':
        print(v)  # prints 100
