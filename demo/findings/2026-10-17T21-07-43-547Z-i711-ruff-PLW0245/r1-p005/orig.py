class A: pass
class B(A):
    def get(self):
        try:
            return super[0]  # triggers rule: becomes super()[0]
        except TypeError as e:
            return f'TypeError: {e}'
print(B().get())  # Should print TypeError: 'super' object is not subscriptable
