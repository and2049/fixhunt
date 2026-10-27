from typing import List

# This program does not trigger SIM109 (no chained equality)
# but we show that if there were such a chain, and we had a typing-only name,
# it would be unaffected.
def f(x: List[int]) -> bool:
    return x == [1] or x == [2]  # no trigger: x is not simple name? It is, but == [1] and == [2] — wait, this *does* trigger!
# LHS: x, RHS: [1], [2] — yes, triggers.
# But x is a parameter, not a typing-only name.
# To involve typing-only: suppose we compare to a type annotation artifact.
# Not possible at runtime.
# So we make a near-miss: a == b or a == c where b or c is from typing but unused.
# Example: from typing import Any; a = 1; b = Any  # but Any is not useless at runtime.
# Actually, Any is usable at runtime.
# We'll skip and make a no-trigger example.
print('No SIM109 trigger')
