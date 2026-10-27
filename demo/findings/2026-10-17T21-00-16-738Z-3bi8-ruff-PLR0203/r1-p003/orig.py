class C:
    def log(msg):
        with open('test.txt', 'w') as fp:
            fp.write(msg)  # expects str
            fp.write(b'\n')  # error: bytes not str
    log = staticmethod(log)

try:
    C.log('hello')
except Exception as e:
    print(type(e).__name__, str(e))
finally:
    import os
    if os.path.exists('test.txt'):
        os.remove('test.txt')
