class C:
    def f():
        return 1
    # This line is invalid syntax; we cannot execute it.
    # Instead, we show that the rule does not trigger on valid code.
    pass
print('no trigger')
