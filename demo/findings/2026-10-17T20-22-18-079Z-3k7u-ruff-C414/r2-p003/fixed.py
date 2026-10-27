def main():
    side_effects = []
    def gen():
        side_effects.append('gen')
        return [1, 2]
    # Rule fires: list(tuple(gen())) inside f-string
    s = f'Result: {list(tuple(gen()))}'
    print(s)
    print('Side effects:', side_effects)
    # Fix would make it f'Result: {list(gen())}' -> gen() called once instead of twice?
    # Actually: tuple(gen()) calls gen() once, then list(...) calls tuple(...) once -> still one gen() call
    # So no change in call count. Need inner arg to be evaluated multiple times?
    # Let's make inner arg a function call with side effect, but tuple() consumes it once.
    # Instead: use expr that is evaluated twice if not nested? No.
    # Hazard: if inner call is something like tuple(f()) and f has side effect, fixing doesn't change # calls.
    # Real hazard: if the inner constructor is avoided, and the arg is used elsewhere.
    # But here, we just want to see if f-string eval order changes.
    # Actually: no. So simulate: make inner arg a tuple of two calls.
    # But rule only fires on tuple(x) where x is expr.
    # Let's do: list(tuple((f(), f())))
    side_effects.clear()
    def f():
        side_effects.append(len(side_effects))
        return len(side_effects)
    s = f'Value: {list(tuple((f(), f())))}'
    print(s)
    print('Side effects:', side_effects)
    # Before fix: f() called twice -> [0,1]
    # After fix: list((f(), f())) -> still two calls
    # No change. 
    # Instead: make inner tuple of a generator that yields side effects
    side_effects.clear()
    def g():
        side_effects.append('yield')
        yield 1
        side_effects.append('yield2')
        yield 2
    s = f'List: {list(tuple(g()))}'
    print(s)
    print('Side effects:', side_effects)
    # tuple(g())) consumes generator fully -> two yields
    # list(tuple(...)) -> same
    # fix: list(g()) -> also consumes fully
    # Still no change.
    # Give up on f-string changing behavior; just show it triggers and runs.
    # But requirement: trace must depend on rewritten code.
    # So we need a case where fixing changes behavior.
    # How about: inner tuple is of a list comprehension that has side effect AND is used later?
    # But tuple() consumes it.
    # Alternative: inner call is tuple of a function that returns a list, and we reuse that list.
    # Not possible.
    # Let's switch to % formatting for clearer order.
    side_effects.clear()
    def h():
        side_effects.append('h')
        return [3, 4]
    s = 'Result: %s' % list(tuple(h()))  # Rule fires
    print(s)
    print('Side effects:', side_effects)
    # Fix: 'Result: %s' % list(h()) -> h() called once either way
    # Still no.
    # Accept that for pure constructor removal, side effects in arg are unchanged.
    # But the assignment says: make trace depend on rewritten code.
    # So we must find a way.
    # Insight: if the inner constructor is not just tuple but list, and we have list(list(x)),
    # then fixing to list(x) changes nothing if x is list.
    # But if x is a tuple, list(tuple(x)) vs list(x) -> same.
    # Unless x is a custom iterable with side effects in __iter__.
    # Let's do that.

class SideEffectIter:
    def __init__(self, data):
        self.data = data
        self.calls = 0
    def __iter__(self):
        self.calls += 1
        print(f'  __iter__ call {self.calls}')
        return iter(self.data)

side_effects.clear()
sei = SideEffectIter([10, 20])
s = f'Iter: {list(tuple(sei))}'  # Rule fires
print(s)
print('__iter__ calls:', sei.calls)
# Before fix: tuple(sei) -> __iter__ called once, list(...) -> __iter__ called again on tuple? No: tuple(sei) consumes sei, then list(...) is called on the tuple -> no second __iter__ on sei.
# So sei.__iter__ called exactly once.
# After fix: list(sei) -> __iter__ called once.
# Same.
# But: tuple(sei) creates a new tuple; its __iter__ is called by list(...).
# So sei.__iter__ still once.
# No change.

# Final attempt: use inner call that is tuple of a list, and we mutate the list between.
# But tuple() snapshots.

print('--- f-string section done ---')

if __name__ == '__main__':
    main()
