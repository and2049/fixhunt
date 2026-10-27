class A:
    def __str__(self): return 'A_str'
    def __bytes__(self): return b'A_bytes'
class B(A):
    def method(self):
        s = super.__str__  # triggers rule: becomes super().__str__()
        if callable(s):
            return s()
        else:
            return str(s)
print(B().method())  # Should print 'A_str'; if broken, returns '<built-in method ...>'
