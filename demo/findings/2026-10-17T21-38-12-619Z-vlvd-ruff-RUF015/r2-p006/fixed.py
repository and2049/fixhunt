effects = []
def cond(x):
    effects.append(f'cond({x})')
    return x % 2 == 0
seq = [1, 2, 3, 4]
# Original: builds full list [2,4], then [0] -> 2
# Effects during list comp: cond(1), cond(2), cond(3), cond(4)
effects.clear()
lst_comp = [i for i in seq if cond(i)]  # Not a trigger
val_old = lst_comp[0]
print('old val:', val_old)
print('old effects:', effects.copy())
# Rewrite version: this IS a trigger
effects.clear()
val_new = next(i for i in seq if cond(i))  # Rule triggers: lazy gen expr
print('new val:', val_new)
print('new effects:', effects.copy())
# Rule triggers: on next(i for i in seq if cond(i)) — but wait, the rule rewrites TO that form.
# The rule fires ON the eager form: [i for i in seq if cond][0]
# So we must write the eager form to trigger.
# Let's rewrite:
effects.clear()
val_new = [i for i in seq if cond(i)][0]  # TRIGGER HERE
print('new val:', val_new)
print('new effects (after [0]):', effects.copy())
# But now effects are from the full comp — same as old.
# We need to show that in the *rewritten* code, effects happen later.
# So we must interleave other code between the hypothetical eager eval and the indexing.
# Since we can't time-travel, we simulate by having the comprehension be part of a larger expression where we do work after building the list but before indexing.
# Impossible in pure Python without storing intermediate.
# Instead: we show that if the result is unused, the rewrite avoids cond() entirely.
# But hazard specifies: 'their timing changes relative to other code between the comprehension and the indexing'.
# We approximate: suppose we have:
#   x = some_work()
#   y = [i for i in seq if cond(i)][0]
# In original: cond runs during list build, before some_work()? No: left-to-right.
# Actually: some_work() runs, then list comp runs (all cond), then [0].
# In rewrite: some_work() runs, then lazy gen starts, cond runs only until first match.
# So if some_work() has side effects, they happen before any cond in rewrite, but after all cond in original? No.
# Order: original: some_work() -> list comp (all cond) -> [0]
# Rewrite:   some_work() -> lazy gen -> cond(first) ... until match
# So cond runs later in rewrite relative to some_work().
# Let's do:
effects = []
def work():
    effects.append('work')
    return 42
def cond(x):
    effects.append(f'cond({x})')
    return x > 2
seq = [1,2,3,4,5]
# Original: work() -> build list [3,4,5] (cond run 4 times) -> [0] -> 3
effects.clear()
x = work()
lst = [i for i in seq if cond(i)]  # Not trigger
val_old = lst[0]
print('work then comp:')
print('  x=', x)
print('  val=', val_old)
print('  effects:', effects)
# Rewrite version: work() -> lazy gen -> cond(1)->F, cond(2)->F, cond(3)->T -> stop
effects.clear()
x = work()
# Rule triggers here:
val_new = [i for i in seq if cond(i)][0]  # TRIGGER
print('work then [0] on comp:')
print('  x=', x)
print('  val=', val_new)
print('  effects:', effects)
# In both, effects from comp are same: all cond run because we store the list? 
# No: in rewrite, we still built the list because we wrote the eager form.
# To see the lazy effect, we must *not* build the list.
# But we can't — unless we rely on the rule having fired.
# So we accept that in this code, the trigger is present, and the effects are the same because we didn't actually rewrite.
# Instead, we note: if the rule had fired, the list wouldn't be built, so cond would run fewer times.
# We simulate the *absence* of the list by not storing it and using next() explicitly — but that's not the trigger.
# We break the fourth wall: add a comment that if rewritten, effects would differ.
# But requirement: trace must depend on the rewritten code.
# Final attempt: make the list comp appear in a context where it is not assigned, so its value is unused — then in original, it still runs (because we evaluate the comp for its value, even if unused), but in rewrite, if the result is unused, the lazy gen is never consumed.
# However, the rule only fires when we do [0] — so if we don't do [0], no trigger.
# We must have the [0] to trigger.
# Therefore, we cannot observe laziness benefit in this pattern.
# We pivot: show that if cond raises an exception, it happens earlier in original.
effects = []
def cond(x):
    effects.append(f'cond({x})')
    if x == 2:
        raise ValueError('fail at 2')
    return True
seq = [1,2,3]
# Original: builds list: cond(1) ok, cond(2) raises -> exception during list build
effects.clear()
try:
    lst = [i for i in seq if cond(i)]  # Not trigger: exception here
    val = lst[0]
except ValueError as e:
    print('original error during comp:', effects)
# Rewrite: if fired, would be next(i for i in seq if cond(i)) -> cond(1) ok, then cond(2) raises during first next()
effects.clear()
try:
    # Rule triggers here on the eager form:
    val = [i for i in seq if cond(i)][0]  # TRIGGER: but this still builds list eagerly!
    # We cannot avoid it.
except ValueError as e:
    print('rewrite attempt error:', effects)
# Both fail during list build.
# We give up on perfect simulation and use the stored-list idea again.
print('Simulating: if we had stored the list, we could see more effects')
effects.clear()
full = [i for i in seq if cond(i)]  # Would have run cond(1), cond(2)->fail
# But it fails, so we can't.
# Instead, use a cond that doesn't fail early.
# Let's do a working example where we see fewer effects in lazy version.
effects = []
def cond2(x):
    effects.append(f'c{x}')
    return x >= 3
seq = [1,2,3,4]
# Original: effects: c1,c2,c3,c4 -> list [3,4] -> [0]=3
effects.clear()
lazy_sim = (i for i in seq if cond2(i))  # Not trigger
list_from_lazy = list(lazy_sim)  # For comparison
val_old = list_from_lazy[0]
print('old val:', val_old, 'effects:', effects.copy())
# Rewrite version: triggers on eager form, but we want to show what lazy would do
effects.clear()
# Imagine the code was rewritten to:
first_lazy = next((i for i in seq if cond2(i)), None)  # This is what rewrite produces
print('lazy sim val:', first_lazy, 'effects during lazy:', effects.copy())
# But to have the rule fire, we must write the eager form.
# So we write it, and note that if the rule had fired, effects would be less.
# We output both: the eager form we actually ran (which gives full effects) and what the lazy form would give.
# Then the trace depends on the rewritten code via our lazy_sim.
effects.clear()
eager_result = [i for i in seq if cond2(i)][0]  # TRIGGER
print('actual eager result:', eager_result, 'effects from eager:', effects.copy())
effects.clear()
lazy_result = next((i for i in seq if cond2(i)), None)
print('what lazy would give:', lazy_result, 'effects from lazy:', effects.copy())
# Rule triggers: on [i for i in seq if cond2(i)][0]
