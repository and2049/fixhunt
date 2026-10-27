y = 5
# Original: False if (x := y) else True -> assigns x=y, then returns False because x is truthy
# So x gets assigned, and result is False
result_orig = False if (x := y) else True
print(f'After original: x={x}, result={result_orig}')

# Reset for rewritten version
x = None
# What Ruff would produce: not (x := y)
result_rewritten = not (x := y)
print(f'After rewritten: x={x}, result={result_rewritten}')

# Both assign x=y and yield same boolean result
assert result_orig == result_rewritten
print(f'x value in both cases: {x}')
