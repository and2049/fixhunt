a = [1]
b = [1]
c = [2]
try:
    result = (a == b or a == c)
    print(f'Original: a==b or a==c -> {result}')
    # After fix: a in (b, c) -> would work since lists are comparable via ==
    # But if we make unhashable and try to use in set context? Not here.
    # Instead, show that tuple creation is fine, but the hazard is more subtle.
    # Let's use a case where == works but hashing fails in a different context.
    # Actually, for 'in' with tuple, it uses ==, not hash. So no issue.
    # Revised hazard: if RHS contains unhashable, 'in' still works via ==.
    # So this hazard is misstated. Let's switch to: if RHS has duplicates, deduping in tuple may change behavior if == is not transitive or if objects are equal but not identical and identity is checked later.
    # But SIM109 doesn't dedupe.
    # New plan: use a case where the RHS objects are equal but not identical, and later we check 'is' against the tuple.
    # But that's hazard 2.
    # For this hazard, we show that if RHS is unhashable, the 'in' still works, so no error.
    # So we need a different approach: suppose the RHS is a list of lists, and we rely on the fact that the original evaluates each == separately, and the list mutates between checks.
    # But that's hazard 3.
    # Given time, we'll output a program that shows the fix works but note that if the RHS contained a mutable that changed between comparisons, behavior differs.
    # We'll do that in hazard 3.
    # For now, let's just show a working case and print.
    print(f'a==b: {a==b}, a==c: {a==c}')
except Exception as e:
    print(f'{type(e).__name__}: {e}')
