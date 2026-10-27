def main():
    # Rule fires on: list(tuple((lambda: [1, 2])()))
    # Inner: tuple( (lambda: [1,2])() ) -> tuple([1,2]) -> (1,2)
    # Outer: list((1,2)) -> [1,2]
    # Fix: list( (lambda: [1,2])() ) -> list([1,2]) -> [1,2]  -> same result
    # Wait, no change in result.
    # But hazard says: "changes the call semantics entirely"
    # How? If we had: tuple(lambda: [1,2]) without calling it, then list(...) would fail.
    # But the pattern is tuple(lambda: [...])() - the lambda is called.
    # Unless... the inner tuple is not around the lambda call but the lambda itself?
    # No: the rule fires on tuple(z) where z is the lambda call.
    # So z = (lambda: [1,2])() -> list of ints.
    # tuple(z) is fine.
    # To change semantics, we need the inner constructor to be applied to something that is not yet called.
    # But the rule requires the inner constructor to have an argument.
    # Unless we do: list(tuple(lambda: [1,2]))  -- no () on lambda
    # Then: tuple(lambda: [1,2]) -> TypeError: 'function' object is not iterable
    # So rule does NOT fire because inner tuple(...) fails at runtime?
    # But rule is static: it sees tuple(lambda: [1,2]) and thinks it might be ok.
    # However, lambda: [1,2] is not iterable, so tuple() raises.
    # But the rule might still fire syntactically.
    # Let's assume it does.
    # Then: before fix: list(tuple(lambda: [1,2])) -> tries to make tuple of function -> TypeError
    # After fix: list(lambda: [1,2]) -> same TypeError
    # Still same.
    # Unless we have: list(tuple((lambda: [1,2])())) vs list((lambda: [1,2])()) 
    # First: inner tuple((lambda: [1,2])()) = tuple([1,2]) = (1,2); outer list -> [1,2]
    # Second: list((lambda: [1,2])()) = list([1,2]) = [1,2]
    # Same.
    # I think the hazard description is misleading.
    # Alternative interpretation: the inner call is a lambda that returns an iterable, and we are doing tuple(lambda_that_returns_iter) without calling it, but that doesn't match the pattern.
    # Given time, I'll implement the call version and note that result is same, but we print to show it runs.
    # But requirement: trace must depend on rewritten code.
    # So we need a difference.
    # How about: if the lambda captures a variable that is mutated, and we rely on the tuple being made vs not?
    # Still: tuple(...) forces evaluation.
    # Let's abandon and do: inner call is tuple of a generator expression that we intend to reuse, but tuple consumes it.
    # Not helpful.
    # Finally: use that the inner tuple is of a list, and we have a custom list subclass where __iter__ has side effect, and we also rely on the type being tuple for something.
    # But after fix, we don't have tuple.
    # Example: we check type of intermediate result.
    # But the intermediate is not stored.
    # Store it.
    try:
        inner = (lambda: [1, 2])()  # [1,2]
        middle = tuple(inner)       # (1,2)  <- this is what rule sees as inner tuple call
        outer = list(middle)        # [1,2]
        print('Triple step:', outer, type(middle).__name__)
    except Exception as e:
        print('Error in triple step:', type(e).__name__, str(e))
    
    # Now the fused version that rule would produce:
    try:
        # This is what fix does: list( (lambda: [1,2])() )
        fused = list((lambda: [1, 2])())
        print('Fused:', fused)
        # But we lost the middle tuple -> can't print its type
    except Exception as e:
        print('Error in fused:', type(e).__name__, str(e))
    
    # To compare, we need to run both versions in same program.
    # Let's define two functions.
    def original():
        return list(tuple((lambda: [1, 2])()))
    def fixed():
        return list((lambda: [1, 2])())
    
    print('Original:', original())
    print('Fixed:', fixed())
    print('Results equal:', original() == fixed())
    
    # Now add side effect to lambda to see if evaluation count changes.
    side_effects = []
    def make_lambda():
        side_effects.append('make')
        return lambda: [side_effects.pop() if side_effects else 0]  # messy
    # Better:
    side_effects.clear()
    def gen_list():
        side_effects.append('gen_list')
        return [1, 2]
    
    def orig():
        return list(tuple((gen_list())))
    def fix():
        return list((gen_list()))
    
    side_effects.clear()
    r = orig()
    print('Original result:', r, 'side effects:', side_effects.copy())
    side_effects.clear()
    f = fix()
    print('Fixed result:', f, 'side effects:', side_effects.copy())
    
    # Both call gen_list once -> same.
    
    # Last idea: inner tuple is of a list, and we have __getitem__ side effect, and we do list(tuple(x))[0] vs list(x)[0]
    # But tuple(x) materializes full tuple, so __getitem__ called len(x) times during tuple creation,
    # while list(x) calls __getitem__ during list creation.
    # Same number.
    
    # I give up on this hazard showing behavior change; will make it trigger and print same result.
    # But must have trace depend on rewritten code.
    # So we will make the lambda return different things based on a counter.
    call_count = 0
    def make_lambda():
        nonlocal call_count
        call_count += 1
        return lambda: [call_count]
    
    f1 = make_lambda()  # returns lambda that gives [1]
    f2 = make_lambda()  # returns lambda that gives [2]
    
    # Original: list(tuple(f1())) -> f1() called once -> [1]; tuple -> (1,); list -> [1]
    # Fixed: list(f1()) -> [1]
    # Same.
    # Unless we do: list(tuple(f1())) vs list(tuple(f2())) but no.
    
    # Use same lambda twice:
    side_effects.clear()
    def make_side_lambda():
        def lst():
            side_effects.append('called')
            return [len(side_effects)]
        return lst
    
    lam = make_side_lambda()  # first call -> [1]
    # Original: list(tuple(lam())) -> lam() -> [1]; tuple -> (1,); list -> [1]
    # Fixed: list(lam()) -> [1]
    # lam() called once either way.
    
    # Call lam twice in different contexts:
    # Original: list(tuple(lam())) + list(tuple(lam()))
    # Fixed: list(lam()) + list(lam())
    # Each calls lam twice.
    
    side_effects.clear()
    lam = make_side_lambda()
    res_orig = list(tuple(lam())) + list(tuple(lam()))
    print('Original:', res_orig, 'side effects:', side_effects.copy())
    side_effects.clear()
    lam = make_side_lambda()  # new lambda
    res_fixed = list(lam()) + list(lam())
    print('Fixed:', res_fixed, 'side effects:', side_effects.copy())
    
    # Both: lam() called twice -> side effects: ['called','called'] -> returns [1], [2] -> [1,2,1,2]
    
    # Still same.
    
    # Conclusion: for this pattern, fixing does not change behavior.
    # But we must output something.
    print('Lambda section completed (results identical in this implementation)')

if __name__ == '__main__':
    main()
