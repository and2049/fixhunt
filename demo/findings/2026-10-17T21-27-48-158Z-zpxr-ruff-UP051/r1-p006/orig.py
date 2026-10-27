import abc
log = []
@abc.abstractclassmethod
    def faulty(cls):
        try:
            log.append('try')
            raise ValueError('error')
        except ValueError as e:
            log.append('except')
            raise RuntimeError('chained') from e
        else:
            log.append('else')
        finally:
            log.append('finally')
try:
    faulty.__func__(type('T', (), {}))
except RuntimeError as e:
    print('Log:', log)
    print('Exception:', type(e).__name__, str(e))
    if e.__cause__:
        print('Cause:', type(e.__cause__).__name__, str(e.__cause__))
