try:
    int('a')
except (ValueError,):
    print('value error caught')
