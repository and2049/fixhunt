def f(lst=[]):
    if lst and lst[0] == True:  # Rule fires here
        lst.clear()
        return 'cleared'
    lst.append(False)
    return lst

print(f())  # First call: lst=[] -> if false -> append False -> [False]
print(f())  # Second: lst=[False] -> lst[0]==True? False -> append -> [False, False]
print(f())  # Third: [False, False] -> still False -> [False, False, False]
# Now set lst[0] = True manually? Can't from outside.
# Let's make it so we pass in a list.
print('---')
def g(lst):
    if lst and lst[0] == True:  # Rule fires
        return 'yes'
    return 'no'

lst = [True]
print(g(lst))  # 'yes'
lst[0] = False
print(g(lst))  # 'no'
# After rewrite: becomes `if lst and lst[0]:`
# For lst=[True]: lst[0] is True -> truthy -> 'yes'
# lst=[False]: lst[0] is False -> falsy -> 'no' -> same.
# Need where truthiness differs from == True.
# Use [1]: 1 == True -> True, and 1 is truthy.
# Use [0]: 0 == True -> False, 0 falsy.
# Use []: error.
# Use [2]: 2 == True -> False, but 2 truthy.
# AHA!
lst2 = [2]
print('Before rewrite equivalent:', g(lst2))  # lst[0]==True -> 2==True -> False -> 'no'
# After rewrite: `if lst and lst[0]:` -> lst=[2] -> lst[0]=2 (truthy) -> 'yes'
# So we simulate by having two versions.
# We'll print what the rewritten version would do.
print('Rewritten would return:', 'yes' if lst2 and lst2[0] else 'no')
