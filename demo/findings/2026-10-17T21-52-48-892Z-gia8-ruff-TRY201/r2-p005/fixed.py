try:
    raise RuntimeError('fail')
except RuntimeError as err:
    raise err
    print(err)
