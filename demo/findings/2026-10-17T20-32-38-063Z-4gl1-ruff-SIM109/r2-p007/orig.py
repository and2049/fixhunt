lst1 = [1, 2]
lst2 = [3, 4]
a = lst1
if a == lst1 or a == lst2:
    matched = lst1 is a  # True only if a is lst1
else:
    matched = False
print('Matched and identity preserved?', matched)
# After fix: a in (lst1, lst2) -> a == lst1 or a == lst2, but tuple is new.
# However, 'is' check above still uses original lst1, so behavior preserved.
# To break: need to check identity of the tuple itself.
tup = (lst1, lst2)
print('Original tuple id:', id(tup))
# Simulate what fix does: creates new tuple
new_tup = (lst1, lst2)
print('New tuple id:', id(new_tup))
print('Same object?', tup is new_tup)
