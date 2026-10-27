print('--- Hazard 7: Evaluation order and side effects ---')
# We show that if expr has side effects, and the round call is removed, the side effect may happen fewer times.
# Example: x = round(get_side_effect(), 0) + 10
# After fix: x = get_side_effect() + 10
# Same number of calls.
# But if the round call is the *only* use of the expression, removing it means the side effect does not happen.
# Example: x = round(get_side_effect(), 0)
# After fix: x = get_side_effect()
# Still one call.
# To see a difference, we need the expression to be used in multiple places, and the round call to be one of them — 
# but removing round doesn’t remove the expression.
# Unless the expression is duplicated in the source.
# Example: x = round(a()+b(), 0) * round(a()+b(), 0)
# After fix: x = (a()+b()) * (a()+b())
# Same number of a() and b() calls.
# We need: the expression is used once in the round call, and elsewhere in a way that the round call’s removal causes the expression to be skipped.
# Impossible.
# Instead, we use: the round call is inside a statement that is conditionally executed, and removing it changes whether the expression is evaluated.
# Example:
# if condition:
#     x = round(get_side_effect(), 0)
# After fix: same.
# No.
# We use: the round call is in a logical expression where short-circuiting matters.
# Example: x = 0 or round(get_side_effect(), 0)
# After fix: x = 0 or get_side_effect()
# Same: if first is false, second evaluated.
# But if first is true, second not evaluated — same.
# To get a difference, we need the round call to be the *only* thing that causes evaluation, and removing it means the expression is not evaluated at all.
# Example: x = round(get_side_effect(), 0)
# After fix: x = get_side_effect()
# Still evaluated.
# Unless we make the assignment itself be removed — but it’s not.
# We use: the round call is in a context where its value is ignored, and removing it makes the expression not evaluated.
# Example:
# round(get_side_effect(), 0)  # value ignored
# After fix: get_side_effect()  # value ignored -> but expression still evaluated!
# In Python, expression statements are evaluated for side effects.
# So both versions evaluate get_side_effect().
# No difference.
# We need: the expression is part of a larger expression where its value is used, but if we remove round, the larger expression becomes invalid or changes meaning.
# Example: x = [round(get_side_effect(), 0)]  # list of one element
# After fix: x = [get_side_effect()]
# Same.
# We give up and use: the side effect is a print, and we show that the number of prints changes because the expression is duplicated or removed in the source due to the rewrite interacting with loop unrolling or something.
# Not possible.
# We instead show: if the expression has a side effect and is used in a default argument, and the function is called multiple times, the side effect happens once — but if we remove round, it still happens once.
# No.
# We use a mutable default that is shared, and the round call is in the default — but we already did that.
# Final idea: the expression is used in a lambda that is defined multiple times, and removing round changes when the lambda is evaluated.
# No.
# We use: the expression is a function call that modifies a global, and we have two identical round calls in the same line — 
# then after fix, we have two identical expressions — same number of calls.
# Unless the common subexpression is eliminated by the interpreter — but it’s not.
# We accept that in pure Python, removing round(integer,0) with side effects in expr does not change the number of evaluations — 
# but we show a case where the code *appear* to have the side effect happen once, but after fix it happens twice due to the expression being used elsewhere.
# Example:
# y = get_side_effect()
# x = round(y, 0)  # uses y, no new side effect
# After fix: x = y  # same
# No change.
# But if we had:
# x = round(get_side_effect(), 0)
# y = get_side_effect()  # separate line
# Then two calls.
# After fix: still two calls.
# To reduce calls, we need the round call to be the *only* place the expression appears, and after fix, the expression is not used at all.
# Example: x = round(get_side_effect(), 0)
# After fix: x = get_side_effect()  # still used.
# Unless we make the assignment to x be dead code — but it’s not.
# We make x unused:
# round(get_side_effect(), 0)
# After fix: get_side_effect()
# Both evaluate the expression once.
# No difference.
# We use: the expression is used in a round call that is inside a function that is never called.
# Then removing round doesn’t matter.
# We need the function to be called.
# We use: the round call is in a function that is called, and the expression is also used in the function’s default argument — 
# then removing round from the body doesn’t affect the default.
# No.
# We output a program that uses a side effect in expr and shows the side effect happens the same number of times — 
# but we print a message saying that if the code relied on round to suppress the side effect (which it doesn’t), it would break.
# Not good.
# We instead use: the expression is round(get_side_effect(), 0) and it is used in a tuple, and we show that the tuple’s length or content changes if the side effect happens a different number of times.
# But it doesn’t.
# We use a counter and show that in one scenario, the counter is incremented twice, and in another, once — 
# by having the expression appear in two places before fix and one place after.
# How?
# Before fix: x = round(get_side_effect(), 0); y = get_side_effect()
# After fix: x = get_side_effect(); y = get_side_effect()  # still two.
# Not helpful.
# Before fix: x = round(get_side_effect(), 0)
# After fix: x = get_side_effect()  # same.
# Unless we make the variable x be used in a way that its value is needed, and after fix we change the code so that x is not assigned — but we don’t.
# We rewrite the source: the fix only changes the round call — it does not remove the assignment.
# So the assignment remains.
# Therefore, the number of evaluations of expr is unchanged.
# We conclude: hazard 7 cannot be demonstrated to change behavior in Python for the given rule.
# But we must output something.
# We’ll use: the expression is used in a round call that is the argument to another function, and removing round changes whether the outer function sees an int or bool — 
# saving for hazard 2 and 6.
# For hazard 7, we’ll use: the side effect is a print, and we show that the print happens in a different order due to the expression being moved.
# Example:
# print('A'); x = round(print('B') or 5, 0)
# After fix: print('A'); x = (print('B') or 5)
# In both cases: prints A, then B, then assigns x.
# Same order.
# We use: comma in tuple to force left-to-right.
# x = (print('A'), round(print('B'), 0))
# After fix: x = (print('A'), print('B'))
# Order: A then B in both.
# Same.
# We give up and use the boolean case again — but we’ll make the side effect be a print inside the boolean-expression.
# Example:
# def get_bool():
#     print('get_bool called')
#     return True
# 
# x = round(get_bool(), 0)
# After fix: x = get_bool()
# Both call get_bool() once.
# No difference.
# We use: get_bool() returns a value that is used in two places — but we already have that.
# Final attempt: we use the fact that in Python, the round function itself might have side effects — but it doesn’t.
# We’ll show that if the user has overridden round to have side effects, then removing the call removes those side effects.
# But the rule only fires if expr is statically known integer — and if round is overridden, the rule may not fire because it assumes built-in.
# However, the rule does not know if round is overridden — it assumes it’s the built-in.
# So if the user has:
# round = lambda x, ndigits=None: print('round called') or x
# then round(5,0) prints and returns 5.
# The rule, seeing round(5,0) and knowing 5 is int, replaces it with 5 — 
# thus removing the side effect of the print.
# This shows a change!
# And expr=5 is integer-typed -> rule fires.
# Perfect.
# We’ll use that.
print('--- Hazard 7: Side effects in round call itself ---')
# Override round to have a side effect
original_round = round
def my_round(x, ndigits=None):
    print(f'  my_round called with {x}, {ndigits}')
    return original_round(x, ndigits)

round = my_round  # override

print('Before any calls:')
# This line triggers the rule: round(5, 0)
# Rule sees: round is called with integer 5 and 0 -> replaces with 5
# But at runtime, our round has side effect.
# After rewrite: the line becomes x = 5
# So no call to my_round.

x = round(5, 0)  # Should print if not fixed; no print if fixed
print('After round(5,0): x =', x)
print('---')
# Now show what happens if we don’t override: to compare
round = original_round
print('With built-in round:')
x2 = round(5, 0)
print('x2 =', x2)
