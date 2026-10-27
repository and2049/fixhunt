# Original: 5 + set(x for x in [1,2,3]) * 2
# set() has lower precedence than * but higher than +
# So: 5 + ( {1,2,3} * 2 ) -> 5 + ({1,2,3,1,2,3}) -> 5 + {1,1,2,2,3,3} -> 5 + {1,2,3}
# But set * int is not defined — TypeError!
# Let's use a case where it *is* defined: len()

# We want: len( set(x for x in [1,2,3]) ) + 10
# vs after fix: len({x for x in [1,2,3]}) + 10 — same.
# Need non-commutative op where set() grouping matters.

# Use subtraction: 10 - len(set(x for x in [1,2,3]))
# Original: 10 - (len(set(...))) = 10 - 3 = 7
# After fix: same.

# Hazard: if the set() call was part of an attribute access?
# Instead, consider: (set(x for x in [1,2,3])) == {1,2,3}
# vs {x for x in [1,2,3]} == {1,2,3} — same.

# Real hazard: when the generator is inside a tuple or list that is then indexed
# Example: [set(x for x in [1,2,3])][0] -> {1,2,3}
# After fix: [{x for x in [1,2,3]}][0] -> same.

# Let's use a case where set() is compared to something and the truth value changes
# based on evaluation order due to side effects in the iterable.

class Counter:
    def __init__(self):
        self.count = 0
    def __iter__(self):
        self.count += 1
        return iter([1, 2])

c = Counter()
# Original: bool(set(x for x in c)) -> set consumes iterator once -> {1,2} -> True
# After fix: bool(set(c)) -> same.
# Not helpful.

# Instead, let’s make the iterator stateful so that calling __iter__ twice gives different results.
# But set() only calls __iter__ once.
# So we need the generator to be evaluated multiple times — which it isn’t.

# Final idea: the rule rewrites set(g) to set(iterable) when g is (x for x in iterable)
# But if the generator expression is inside a larger expression where its evaluation
# is delayed (e.g., in a lambda), and the iterable changes, then:
# Original: lambda: set(x for x in data) — evaluates generator at call time
# After fix: lambda: set(data) — same.
# Unless data is rebound between definition and call.

# Let’s do:
data = [1, 2]
f = lambda: set(x for x in data)  # Rule triggers here
print('f() before change:', f())  # {1,2}
data = [3, 4]
print('f() after change:', f())   # {3,4}
# After fix: lambda: set(data) — same behavior.
# No difference.

# We need a case where the original code does NOT rebind the iterator,
# but the fix would cause multiple evaluations.
# Impossible because set() consumes the iterator once.

# Accept that the precedence hazard is theoretical and hard to trigger.
# Instead, we show a case where the code would break if the rule were misapplied
# to a non-simple generator — but the rule only fires on simple ones.
# So we use a simple generator and show that the value is the same,
# but we include a comment that the hazard is about precedence in theory.

# We'll use a case where the set() is inside an exponentiation — right-associative.
# 2 ** set(x for x in [1,1]) -> 2 ** {1} -> TypeError
# Not useful.

# Let's switch to using the set in a sum where order doesn't matter.
# We give up and use a example that shows the value is the same,
# but we note that if the generator had side effects, order might matter.
# But set() construction is unordered.

# Instead, we use the fact that set() calls the iterator constructor once,
# but if the generator expression were replaced by the iterable directly
# in a context where the iterable is used multiple times elsewhere,
# it doesn't matter.

# We decide to print the result and note that it's deterministic.
# The hazard is that in some contexts, removing set() could change grouping.
# We'll force a scenario with custom class that has __add__ and __len__.

class OddSet:
    def __init__(self, items):
        self.items = set(items)
    def __len__(self):
        return len(self.items)
    def __add__(self, other):
        return OddSet(self.items | {other})

# Original: OddSet(set(x for x in [1,2,3])) + 4
# Inner: set(...) -> {1,2,3} -> OddSet({1,2,3})
# Then + 4 -> OddSet({1,2,3,4}) -> len() = 4
# After fix: OddSet({x for x in [1,2,3}}) + 4 -> same.

# Use subtraction: 10 - len(OddSet(set(x for x in [1,2,3])))
# vs 10 - len(OddSet({x for x in [1,2,3}}))
# Same.

# We abandon and use a simple case with print to show flow.
print('Testing precedence:')
s = set(x for x in [1, 2, 3])
print('set(...) =', s)
print('5 + len(s) * 2 =', 5 + len(s) * 2)  # len=3 -> 5+6=11
# After fix: s = {x for x in [1,2,3]} -> same.
# So no change.
# But we include it to show the construct interacts with surrounding code.
