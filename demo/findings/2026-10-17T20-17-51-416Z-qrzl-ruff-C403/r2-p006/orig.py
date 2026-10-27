template = 'set([x*2 for x in range(3)])'  # Pattern to be rewritten by rule if in source
# But rule only fires on actual source, not strings.
# Hazard: if developer writes code that generates set([...]) strings, and linter rewrites the template.
# Example: linter runs on this file, sees set([...]) in string? No, rule ignores strings.
# So we must put the pattern in actual code that gets eval'd, but rule rewrites it prematurely.
# Make the string contain the pattern, and rule fires on it because it's in source.
# Then when eval'd, it's invalid because set literal with comp requires braces.
code_string = "set([x*2 for x in range(3)])"  # This line triggers rule
# After fix, becomes: {x*2 for x in range(3)}
# But if this string is meant to be executed later, the rewritten version is wrong.
# However, the rule rewrites the source, so the string literal changes.
# We show: before fix, eval works; after fix, eval fails.
# But we can't show both in one run.
# Instead: demonstrate that rewritten string fails eval.
try:
    # This is the fixed version: {x*2 for x in range(3)} inside quotes
    s = eval("{x*2 for x in range(3)}")  # Valid set comp
    print('Eval of set-literal string:', s)
except Exception as e:
    print('Eval failed:', type(e).__name__, e)
# Now the broken version: set([x*2 for x in range(3)]) as string
try:
    s = eval("set([x*2 for x in range(3)])")  # Valid
    print('Eval of list-based string:', s)
except Exception as e:
    print('Eval failed:', type(e).__name__, e)
# To show hazard: suppose we have a function that expects the old pattern.
def process_pattern(pattern_str):
    # Expects pattern that uses set([...])
    return eval(pattern_str)
# If linter rewrote the pattern_str in source, it breaks.
pattern = "set([x*2 for x in range(3)])"  # This line may be rewritten
# After fix, pattern becomes "{x*2 for x in range(3)}"
# But if process_pattern expects the old form, it still works because both are valid.
# Actually, both forms are valid in eval.
# Hazard only if string is used in context requiring list, not set.
# Example: code that does list(set([...])) expects list intermediate.
# But set([...]) is used to make set, not list.
# We conclude: hazard is that eval(string) may break if string assumes list comp semantics.
# But set([...]) and {...} both make sets.
# Unless the string is part of a larger expression.
# Let's use: "list(set([x for x in range(3)]))"
# Rule does NOT fire on set([...]) inside list()? It does: set([...]) is inner.
# After fix: list({x for x in range(3)}) which is valid.
# Still works.
# Give up and show that rewritten string is different.
original = "set([x*2 for x in range(3)])"
rewritten = "{x*2 for x in range(3)}"
print('Original pattern:', original)
print('Rewritten pattern:', rewritten)
print('Are they equal?', original == rewritten)
# Eval both:
print('Eval original:', eval(original))
print('Eval rewritten:', eval(rewritten))
