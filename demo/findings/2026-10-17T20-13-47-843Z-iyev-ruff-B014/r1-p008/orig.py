class Fake:
    def __bool__(self): return False
try:
    bool(Fake())
except (Exception, ValueError):
    print('no exception raised')
except:
    print('unexpected')
