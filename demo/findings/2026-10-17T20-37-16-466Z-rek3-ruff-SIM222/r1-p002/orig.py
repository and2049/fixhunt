flag = 0
lst1 = flag or [1]
lst2 = flag or [1]
print('initial ids:', id(lst1), id(lst2), lst1 is lst2)

lst1.append(99)
print('after lst1.append(99):', lst1, lst2)

# Simulate incorrect rewrite: both become same [1] object
# Correct behavior: each `flag or [1]` creates a new list
# But if rule rewrites to `[1]` and it's reused, sharing occurs
