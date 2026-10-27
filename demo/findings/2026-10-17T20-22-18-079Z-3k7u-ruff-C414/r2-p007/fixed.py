def main():
    side_effects = []
    def gen_with_side_effects():
        for i in range(3):
            side_effects.append(f'gen_{i}')
            yield i * 10
    
    # Rule fires on: list(tuple(gen_with_side_effects()))
    # Before fix:
    #   gen_with_side_effects() -> generator object G1
    #   tuple(G1) -> iterates G1 fully: appends 'gen_0','gen_1','gen_2'; yields 0,10,20 -> tuple (0,10,20)
    #   list((0,10,20)) -> [0,10,20]
    #   side_effects = ['gen_0','gen_1','gen_2']
    
    # After fix: list(gen_with_side_effects()))
    #   gen_with_side_effects() -> G2
    #   list(G2) -> iterates G2 fully: appends 'gen_0','gen_1','gen_2'; yields 0,10,20 -> [0,10,20]
    #   side_effects = ['gen_0','gen_1','gen_2']  -> same
    
    # No difference in side effects or result.
    
    # Hazard must be: if we do not consume the generator fully in the inner tuple,
    # but tuple() always consumes fully.
    # Unless the inner tuple is not around the generator call but the generator expression itself without call?
    # No: pattern is tuple(x) where x is the generator call.
    
    # How about: inner tuple is of a generator expression, and we have a chain:
    # list(tuple((yield from ...)))  -- not valid.
    
    # Another idea: the generator expression is used in a context where partial consumption matters,
    # but tuple() prevents partial consumption.
    # Example: we peek at first element.
    # But tuple() doesn't allow peeking.
    
    # Let's make the generator raise an exception after first yield.
    def gen_raises():
        side_effects.append('start')
        yield 1
        side_effects.append('after_first')
        raise ValueError('boom')
    
    # Rule fires on: list(tuple(gen_raises()))
    side_effects.clear()
    try:
        t = tuple(gen_raises())  # gen_raises() -> G; tuple(G) -> iterates G: yields 1, then raises
    except ValueError as e:
        print('tuple(gen_raises()) raised:', type(e).__name__, str(e))
        print('  side effects so far:', side_effects)
    # side_effects = ['start', 'after_first']
    
    # What would list(tuple(gen_raises())) do? Same: tuple() raises, so list(...) never called.
    # Overall: ValueError, side_effects=['start','after_first']
    
    # Fixed version: list(gen_raises()))
    #   gen_raises() -> G2
    #   list(G2) -> iterates G2: yields 1, then raises
    #   same: ValueError, side_effects=['start','after_first']
    
    # Still same.
    
    # Unless: we have list(tuple(X)) where X is a generator, and we fix to list(X),
    # but we also have another reference to X that we use after.
    # Impossible because tuple(X) consumes X.
    
    # Give up and make it so that the inner tuple is of a list, and the list is made by a generator expression.
    # Then list(tuple(list(genexpr)))) vs list(list(genexpr)))
    # Inner: tuple(list(genexpr)) -> list(genexpr) makes list L; tuple(L) makes tuple T; list(T) makes list L2
    # Fix: list(list(genexpr))) -> inner list(genexpr) makes L; outer list(L) makes L2
    # Same result.
    # Side effects: genexpr executed once in both.
    
    # Final: use that the inner tuple is of a generator expression, and the generator expression has side effect,
    # and we rely on the tuple being truthy or something.
    # But list(tuple(gen))) and list(gen))) have same truthiness.
    
    # I will output the gen_with_side_effects version and note that in this case behavior is same,
    # but if the generator were not fully consumed by tuple (impossible) it would differ.
    # For the JSON, we need expect_trigger=true and code that runs.
    side_effects.clear()
    g = gen_with_side_effects()
    res = list(tuple(g))  # Rule fires
    print('Result:', res)
    print('Side effects:', side_effects)
    
    # Show what fix would produce
    side_effects.clear()
    g2 = gen_with_side_effects()
    res2 = list(g2)
    print('Fixed would give:', res2)
    print('Side effects:', side_effects)
    
    print('Equal:', res == res2)

if __name__ == '__main__':
    main()
