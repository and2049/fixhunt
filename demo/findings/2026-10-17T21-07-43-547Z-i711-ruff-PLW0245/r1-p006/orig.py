class A:
    def hello(self, x): return f'A:{x}'
class B(A):
    def hello(self, x):
        # super is a callable that returns a super proxy; super(x) tries to call proxy with x -> error
        # super() returns proxy, then super()(x) tries to call proxy with x -> same error? 
        # Actually: super is NOT callable in this context — super() is the proxy.
        # But the *original* super (without parens) IS callable: it returns a super proxy.
        # So super(x) == super()(x) ???
        # Let's test:
        try:
            return super(x)  # triggers rule: becomes super()(x)
        except Exception as e:
            return f'{type(e).__name__}: {e}'
print(B().hello(42))  # Both should fail same way — but if rule misfires on non-call? Wait.
# Actually: super is always a callable (built-in type). super(x) is valid: returns super proxy for MRO starting after x.
# super() is invalid: no args -> proxy for self.__class__. Then super()(x) tries to call proxy with x -> TypeError.
# So: super(42) works; super()(42) fails.
