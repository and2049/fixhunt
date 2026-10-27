flag = 0
x = []
y = {}
result = x or flag or y
print('result:', result)
# After rewrite (if misapplied): result = x or flag -> []
# Correct: flag=0 (falsy), then y={} -> result = {}
