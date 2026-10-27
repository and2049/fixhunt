from builtins import super as s
class A:
    def attr(self): return 'A_attr'
class B(A):
    def attr(self):
        return s.attr  # triggers rule on 's.attr'? NO — but if rule mistakenly sees 's' as super, it breaks
try:
    print(B().attr())  # prints 'A_attr' if correct; fails if rule broke s into s()
except Exception as e:
    print(f'{type(e).__name__}: {e}')
