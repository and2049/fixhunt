class C:
    @staticmethod
    def f() -> 'return_f()':
        pass
    def return_f():
        return f

try:
    C.f()
except Exception as e:
    print(type(e).__name__, str(e))
