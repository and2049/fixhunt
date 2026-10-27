lists = [[1, 2], [3, 4]]
result1 = sum(lists, [])  # outer lists
for lists in [[5, 6]]:  # shadows outer lists
    result2 = sum(lists, [])  # inner lists
print(result1, result2)
