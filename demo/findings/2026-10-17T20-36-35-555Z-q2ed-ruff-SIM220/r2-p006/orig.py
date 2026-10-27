debug = {'value': True}
if debug['value'] and not debug.__setitem__('value', False) or True:
    print('inside')
else:
    print('outside', debug['value'])
