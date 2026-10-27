list = lambda x: [x*2]  # Shadow list early
data = [1, 2, 3]
# Rule triggers here: uses current 'list' (the lambda)
result = list(data)[0]
print('result:', result)
# Restore built-in to show difference
 del list
result2 = [data[0]*2][0]  # What it would be with built-in list
print('expected with built-in:', result2)
# Rule triggers: on list(data)[0]
