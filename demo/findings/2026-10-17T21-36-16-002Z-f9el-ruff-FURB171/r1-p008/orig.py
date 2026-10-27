y = 5
# This is [*[y]] -> [5], but not a literal; rule should NOT trigger
print(5 in [*[y]])  # True
# Rule does not fire here because container is not a literal
# If incorrectly fixed to 5 == [*[y]][0], that would be valid but rule shouldn't touch it
# So we show it works as-is
print('No rule trigger expected')
# Also test near-miss: x in [y, *[]] -> [y] if y defined
print(5 in [y, *[]])  # [5] -> True
# Still not literal
# x in [*()] -> empty
print(5 in [*()])  # False
