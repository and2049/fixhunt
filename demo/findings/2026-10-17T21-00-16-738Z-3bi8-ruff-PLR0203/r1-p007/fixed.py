class C:
    @staticmethod
    def fails():
        try:
            raise ValueError('bad')
        finally:
            raise RuntimeError('worse')

try:
    C.fails()
except Exception as e:
    print(type(e).__name__, str(e))
