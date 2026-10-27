lst = [1, 2, 3]
result = [] and lst
print('result:', result)
# After fix: result = []
# Original: evaluates [], returns [] (falsey), short-circuits, lst not touched
print('lst unchanged:', lst)
