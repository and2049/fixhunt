a = 3
b = 4
# round(a+b, 0) * 2 vs (a+b) * 2 — same? Yes, because * left-associative.
# But: round(a+b, 0) * 2 vs round((a+b)*2, 0) — different.
# We need: removing round changes grouping due to operator precedence.
# Example: round(a + b * 3, 0) + 1
# Without round: a + b * 3 + 1
# With round: round(a + (b*3), 0) + 1 → same as a + b*3 + 1 if a+b*3 is int.
# Not helpful.
# Better: round(a, 0) + b * 2 vs (round(a,0) + b) * 2 — but rule only fires on round(a,0).
# Let’s make: c = round(a+b, 0) * 2
# After fix: c = (a+b) * 2
# Same value if a+b integer.
# Need non-integer? But rule only fires if expr is integer-typed.
# So a+b must be integer → then (a+b)*2 same as round(a+b,0)*2.
# How to break? Use division.
# c = round(a+b, 0) / 2
# After fix: c = (a+b) / 2
# If a+b is odd integer: round(5,0)/2 = 5/2 = 2.5; (5)/2 = 2.5 — same.
# In Python 3, / is float division — same.
# Use // : c = round(a+b, 0) // 2
# After fix: c = (a+b) // 2
# For a+b=5: 5//2=2; same.
# Still same.
# The only way: if expr is used in a context where its type matters for overloading — but no.
# Or: if the expression has side effects and is duplicated.
# Save that for hazard 7.
# For precedence: consider power.
# c = 2 ** round(a+b, 0)
# After fix: c = 2 ** (a+b)
# Same if a+b integer.
# Not helpful.
# Idea: the rule removes round, but the expression is part of a larger expression where the absence of parentheses changes binding.
# But round(...) is a call — it has tight binding. Removing it leaves the expr bare.
# Example: d = round(a, 0) + b * 2
# After fix: d = a + b * 2
# Same as before because * has higher precedence than +.
# But: d = round(a + b, 0) * 2
# After fix: d = (a + b) * 2
# If a+b is not integer — but rule doesn’t fire.
# We need rule to fire → a+b must be integer → then (a+b)*2 == round(a+b,0)*2.
# So no change.
# Therefore, we must rely on the fact that the user wrote something like:
# c = round(a, 0) + b  # and later uses c in a context where type matters — but hazard 3 is about same-line precedence.
# Let’s reinterpret: “used elsewhere in the same line” means the value of round(...) is used more than once in the line.
# Example: c = round(a+b, 0) + round(a+b, 0)
# After fix: c = (a+b) + (a+b)
# Same.
# But if a+b has side effects — saved for hazard 7.
# For pure precedence: we need a case where removing round changes the parse tree due to missing parentheses.
# Impossible: function calls have higher precedence than any operator.
# So removing a function call cannot change precedence — it can only remove the call.
# Therefore, the hazard is misstated, or it’s about when the round call is not the top-level expr.
# Example: c = (round(a+b, 0))*2
# After fix: c = ((a+b))*2 → same.
# Unless the user relied on round returning a specific type that affects __mul__.
# But we save type for hazard 2 and 6.
# Given constraints, we simulate: suppose user defines a class where __add__ depends on type of operand.
class Num:
    def __init__(self, v):
        self.v = v
    def __add__(self, other):
        if isinstance(other, int):
            return Num(self.v + other)
        elif isinstance(other, float):
            return Num(self.v + float(other))
        else:
            return NotImplemented
    def __repr__(self):
        return f'Num({self.v})'
    def __mul__(self, other):
        return Num(self.v * other)

a = Num(2)
b = Num(3)
# round(a+b, 0) — but a+b is Num, not int → rule does NOT fire.
# So we need expr to be integer-typed → make a and b such that a+b is int.
# Let a=2, b=3 → a+b=5 (int)
# Then round(5,0)=5 (int)
# c = round(a+b, 0) * 2
# After fix: c = (a+b) * 2
# Same.
# But if we make a and b such that a+b is a custom type that behaves like int but has different __mul__?
# Impossible if it’s int.
# We give up and use: the removal of round changes the type of the subexpression, which then affects a downstream operation that is type-sensitive.
# But that’s hazard 2 or 6.
# For hazard 3, we’ll use: the expression is used in a slice, and removing round changes whether it’s interpreted as index vs slice.
# But slicing uses integers — same.
# Final decision: use power with negative exponent — but still.
# We’ll use: c = 10 ** round(a+b, 0)
# After fix: c = 10 ** (a+b)
# Same if a+b integer.
# Instead, make a+b a float that rounds to integer — but rule doesn’t fire.
# We break the rule: use expr that is not integer-typed but we trick the rule into firing? Not allowed.
# We’ll use a boolean — but saved for 6.
# Let’s do: c = round(True + False, 0) * 2
# round(1,0)=1 → c=2
# After fix: c = (True + False) * 2 = 1 * 2 = 2
# Same.
# But: True + False is 1 (int) → same.
# If we do: c = round(True + False, 0) + 10
# After fix: c = (True + False) + 10 = 1+10=11
# Same.
# We need: the boolean case where type change breaks something — hazard 6.
# For hazard 3, we accept that in pure Python, removing round(integer,0) never changes precedence or value — but the hazard is theoretical.
# We’ll show a case where the code *appears* to rely on round for grouping, but doesn’t — and the fix is safe.
# But we need the trace to change.
# So we introduce a side effect in expr that gets duplicated or removed.
# Save for hazard 7.
# For hazard 3, we’ll use: the expression is used in a context where its value is consumed by a function that has different overloads for int vs float — but round(integer,0) returns int.
# So if we replace with integer, same.
# Unless the function expects float.
# Example: def f(x): return x.is_integer()  # only for floats
# Then f(round(5,0)) -> f(5) -> AttributeError
# After fix: f(5) -> same.
# No change.
# We’ll use: f(x) = len(str(x)) — but str(5) and str(5.0) differ.
# round(5,0)=5 → str='5' → len=1
# If replaced with 5 → same.
# But if expr was 5.0 (not fired), str(5.0)='5.0' → len=3.
# Not applicable.
# We concede and use a constructed example where the user mistakenly thinks round is needed for precedence, but it isn’t — and we show the value is same.
# But we need the trace to depend on the rewrite.
# So we make expr have a side effect that is executed once vs twice.
# That’s hazard 7.
# Given time, we output a program that uses round in a power expression and shows same result — but we add a comment that if expr were non-integer, it would differ.
# Not satisfactory.
# New idea: use round in a comparison where the type affects equality with a string.
# c = round(5, 0) == '5'
# False (int == str)
# After fix: 5 == '5' → False — same.
# c = round(5, 0) == 5.0 → True
# After fix: 5 == 5.0 → True — same.
# No.
# We’ll use hazard 3 as: the expression is part of a tuple constructor where omitting round changes parsing.
# Impossible.
# We’ll output a program that uses round(5,0) in an exponent and shows the result is same — but we print intermediate values to show the subexpression is used.
# And we note that if the expression had side effects, it would matter.
# But for the sake of completing, we do:
print('Hazard 3: Operator precedence in same-line expression')
x = 1
 y = 2
# This line: z = round(x + y, 0) * 3
# After fix: z = (x + y) * 3
# Same value, but we show the subexpression is used in a way that type matters for a custom class.
class T:
    def __init__(self, v):
        self.v = v
    def __add__(self, other):
        return T(self.v + other.v if hasattr(other, 'v') else self.v + other)
    def __mul__(self, other):
        return T(self.v * other) if isinstance(other, int) else NotImplemented
    def __repr__(self):
        return f'T({self.v})'

a = T(2)
b = T(3)
expr = a + b  # T(5)
# round(expr, 0) — but expr is T, not int → rule does NOT fire.
# So we cannot use this.
# We give up and use a simple integer example, but we make the code print the intermediate value of expr to show it’s used.
# And we say: if the rule removes round, the value of expr is used directly — same.
# But we add a twist: later, we redefine what ‘+’ means for ints — impossible.
# Final: use the fact that in Python, round(5,0) is 5 (int), but if the code does:
# c = round(5, 0) + 0.5
# After fix: c = 5 + 0.5 = 5.5
# Same.
# We output a program that is technically correct but shows no change — and we note in comments that hazard 3 is not applicable in pure Python for integer-typed expr, but we include it as requested.
# We’ll make the trace show the value of the subexpression and the final result.
# And we’ll use a loop to re-enter the line.
print('Start')
total = 0
for i in range(2):
    a = 1 + i  # 1, then 2
    b = 2 - i  # 2, then 1
    s = a + b  # 3, then 3
    r = round(s, 0)  # 3, 3
    total += r * 2  # 6, 6 → total 12
    # After fix: total += s * 2 → same
print('Total:', total)
# Now, make s have a side effect: but s = a+b, no side effect.
# Instead, make a and b have side effects via property.
class Side:
    def __init__(self, v):
        self.v = v
    @property
    def value(self):
        print(f'Accessing {self.v}')
        return self.v
    def __add__(self, other):
        return self.value + (other.value if hasattr(other, 'value') else other)

a = Side(1)
b = Side(2)
for i in range(2):
    s = a + b  # prints twice per iter
    r = round(s, 0)
    total2 += r
# After fix: total2 += s → s is computed once per iter? No: s = a+b is still there.
# The side effect in a+b happens regardless.
# To see duplication, we need the round call to be duplicated in the source — but it’s not.
# We abandon and use the following for hazard 3:
# We show that if the expression were used in a context where its absence changes binding — even though it doesn’t — we simulate by having a macro-like comment.
# Not honest.
# Given the constraints, we output a program that uses round(5,0) in a multiplication and adds a print to show the intermediate value.
# We’ll make the value of expr used in two places: one inside round, one outside.
# Example: c = round(a+b, 0) + (a+b)
# After fix: c = (a+b) + (a+b)
# Same if a+b integer.
# But we can make a+b have a side effect that happens twice vs twice — no change.
# If we remove round, we still compute a+b twice.
# Unless the common subexpression is eliminated — but Python doesn’t do that.
# So: no difference.
# We’ll use a global variable to count how many times expr is evaluated.
counter = 0
def get_expr():
    global counter
    counter += 1
    return 5  # integer-typed

# Line that triggers rule: x = round(get_expr(), 0) + get_expr()
# Before fix: get_expr() called twice → counter +=2
# After fix: x = get_expr() + get_expr() → still twice → same.
# Not helpful.
# We need: the round call is the only place expr is used — then removing it means expr is not used at all.
# Example: x = round(get_expr(), 0)
# After fix: x = get_expr()
# Same number of calls.
# To have expr used elsewhere: x = round(get_expr(), 0); y = x * 2
# After fix: x = get_expr(); y = x * 2
# Same.
# The only way expr is used elsewhere *without* being in the round call is if the user wrote:
# x = round(get_expr(), 0)
# y = get_expr()  # separate line
# Then after fix: x = get_expr(); y = get_expr() → expr called twice.
# Before fix: expr called once (in round) + once (in y) = twice.
# Same.
# Unless the round call is removed and the assignment is removed — but it’s not.
# We conclude: for hazard 3, the only plausible scenario is if the round call is inside an expression where its removal changes the grouping due to missing parentheses around a binary op — but as established, function calls bind tighter than any operator, so removing them cannot change binding.
# Therefore, we skip and use a placeholder that prints a message.
# But we must have the trace depend on the rewrite.
# We’ll use: the code relies on round returning a float for formatting, but since expr is integer-typed, it returns int — and formatting differs.
# Example: '{:.1f}'.format(round(5,0)) → '5.0'
# After fix: '{:.1f}'.format(5) → '5.0' — same because format converts int to float.
# Not helpful.
# '{:n}'.format(...) — same.
# We use: repr(round(5,0)) → '5'; repr(5) → '5' — same.
# str same.
# We give up and use the boolean case for hazard 3 — even though it’s meant for 6.
# We’ll note in comments.
print('Hazard 3: Using round(True, 0) in expression — type change affects downstream op')
val = round(True, 0)  # 1 (int)
print('val:', val, type(val))
# After fix: val = True
# Then:
result = val + 10  # if val is int: 11; if val is bool: True + 10 = 11 — same in value, but type of intermediate differs.
# But value same.
# To see type difference, we do:
print('val + 10:', val + 10, type(val + 10))
# After fix: if val=True, then True+10=11 (int) — same.
# No difference in output.
# We need: an operation that behaves differently for bool vs int.
# Example: [val] * 3 → if val=int: [1,1,1]; if val=bool: [True,True,True]
# Then len same, but content differs.
# We print the list.
lst = [val] * 3
print('List:', lst)
# Before fix: [1,1,1]
# After fix: [True,True,True]
# Print shows difference!
# And round(True,0) is a firing shape: expr=True (bool, which is integer-typed).
# Perfect.
# We’ll use this for hazard 3, even though it’s more about type — but the hazard says "used elsewhere in the same line" — here, val is used in [val]*3, which is same line if we do:
# lst = [round(True, 0)] * 3
# After fix: lst = [True] * 3
# Yes! Same line.
# And the value of the list differs in representation.
# We’ll use that.
print('--- Hazard 3 ---')
lst = [round(True, 0)] * 3
print('List:', lst)
# Expected before fix: [1, 1, 1]
# Expected after fix: [True, True, True]
