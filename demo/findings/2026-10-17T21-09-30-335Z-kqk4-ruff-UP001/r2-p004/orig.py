class ExceptionTest:
    __metaclass__ = type
    def faulty_method(self):
        try:
            x = 1 / 0
        except ZeroDivisionError as e:
            try:
                raise ValueError('bad') from e
            except ValueError as ve:
                print('Caught:', type(ve).__name__, str(ve))
                raise
        else:
            print('no error')
        finally:
            print('finally')

try:
    ExceptionTest().faulty_method()
except ValueError as e:
    print('Outer caught:', type(e).__name__, str(e))
