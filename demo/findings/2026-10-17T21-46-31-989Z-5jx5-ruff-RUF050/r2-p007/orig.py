x = 5
y = 2
if x / y > 2:  # 2.5 > 2 -> True
    pass
print('Division result:', x / y)
print('Comparison outcome:', x / y > 2)
# If rule duplicates condition, division re-evaluated (same result, but hazard is expression reuse)
