try:
    exec("s = {[x for x in [1,2]]}")
    print('no error')
except SyntaxError as e:
    print(type(e).__name__, str(e))
