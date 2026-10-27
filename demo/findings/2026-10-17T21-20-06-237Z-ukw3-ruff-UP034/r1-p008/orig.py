try:
    raise (Exception('test'))
except Exception as e:
    print('Raised caught:', type(e).__name__, str(e))
