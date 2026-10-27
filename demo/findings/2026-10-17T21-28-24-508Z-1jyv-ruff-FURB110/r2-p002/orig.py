def gen():
    yield 1
    yield 2
    yield 3
g = gen()
a = next(g, None)  # consumes first value
result = g if g else []  # g is now exhausted after first next(), so truthy? No: generator object is always truthy even if exhausted!
# Wait: generator object is truthy regardless of state. So 'g if g else []' always returns g (the generator object), never [].
# This does not trigger FURB110 because condition is 'g' (generator object), which is truthy, but the rule requires condition == true branch.
# Here true branch is 'g', condition is 'g' -> yes, it matches.
# But the value of g is the generator object, not its contents. So we need to inspect what happens.
# Let's change: make condition be the generator's exhaustion state via a function that returns truthy based on state.
# Redo.
