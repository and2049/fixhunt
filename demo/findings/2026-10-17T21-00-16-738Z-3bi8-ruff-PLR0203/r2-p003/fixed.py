class Writer:
    def write(self, s):
        print(s, end='')
class C:
    @staticmethod
    def log(msg):
        w = Writer()
        w.write(msg)
C.log('hello')
print('done')
