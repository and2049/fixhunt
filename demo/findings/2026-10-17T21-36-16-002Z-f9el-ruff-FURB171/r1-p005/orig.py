def append_val(val, lst=[]):
    lst.append(val)
    return lst
# Rule triggers: check if 0 in append_val(0)
first = append_val(0)
print(0 in first)  # True: first is [0]
second = append_val(0)  # now [0,0]
print(0 in second)  # True
# After fix: would be 0 == append_val(0)[0]
# First call: append_val(0) returns [0]; [0][0] = 0; 0==0 -> True
# Second call: append_val(0) returns [0,0]; [0,0][0] = 0; 0==0 -> True
# Same. Need where container mutation makes equality fail but containment pass.
# Use NaN in default.
def add_nan(lst=[]):
    lst.append(float('nan'))
    return lst
nan = float('nan')
# Rule triggers: check if nan in add_nan()
first = add_nan()  # [nan]
print(nan in first)  # True
print(nan == first[0])  # False
# After fix, rule would rewrite nan in add_nan() to nan == add_nan()[0]
# Which would print False instead of True
# So to see difference, we need to print both versions.
# But we can't print both in same run without calling add_nan twice.
# First call for 'in' version:
in_result = nan in add_nan()  # add_nan called -> returns [nan]; nan in [nan] -> True
# Second call for '==' version (simulating fixed code):
equal_result = nan == add_nan()[0]  # add_nan called again -> returns [nan]; nan == nan -> False
print(f'in result: {in_result}')
print(f'== result: {equal_result}')
# Output: True then False
