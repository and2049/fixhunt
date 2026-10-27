try:
    raise ValueError(u'error')
except ValueError as e:
    print(e.args)
finally:
    print('cleanup')
