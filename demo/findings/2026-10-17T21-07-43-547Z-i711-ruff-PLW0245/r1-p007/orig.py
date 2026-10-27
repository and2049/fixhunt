class A:
    def m(self): return 1
class B(A):
    def m(self):
        f = lambda: (s := super).m()  # triggers rule on 's.m()'? s is lambda return — no.
        # Let's put trigger inside lambda:
        g = lambda: super.m()  # triggers: becomes super().m()
        h = lambda: (yield super.m())  # same
        # But we need side effect: capture changing super
        shadows = []
        for i in range(2):
            if i == 1:
                super = 99  # shadow in loop
            shadows.append(lambda: super.m() if callable(super) else f'shadow:{super}')
        return shadows[1]()  # second lambda captures i=1 -> super=99
print(B().m())  # If rule fired on super.m() in lambda, it becomes super().m() -> still uses closed-over super (99) -> AttributeError
# But if rule did NOT fire, super.m() uses the built-in super -> 1
# We want: if rule fires, we get AttributeError (because 99 has no m); if not, we get 1.
# However, the lambda is defined in loop scope — super is looked up at call time.
# At i=1, super=99 in loop, so lambda sees super=99.
# If rule rewrote super.m() to super().m(), then at call: super() -> 99() -> TypeError: 'int' not callable
# If not rewritten: super.m() -> 99.m() -> AttributeError
# So we distinguish:
