try:
    if b'a' < 'b' and 'b' < b'c':
        print('unreachable')
    except TypeError as e:
        print('TypeError:', e)
except Exception as e:
    print(type(e).__name__, e)
