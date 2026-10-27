class A:
    def method(self): return 'A'
class B(A):
    def method(self):
        super = lambda: None  # shadow
        try:
            return super.method()  # triggers rule: should become super().method()
        except AttributeError as e:
            return f'AttributeError: {e}'
        except TypeError as e:
            return f'TypeError: {e}'
print(B().method())
