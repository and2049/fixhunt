class Writer:
    def write(self, s):
        print(s, end='')
class C:
    def log(msg):
        w = Writer()
        w.write(msg)
    log = staticmethod(log)
C.log('hello')
print('done')
