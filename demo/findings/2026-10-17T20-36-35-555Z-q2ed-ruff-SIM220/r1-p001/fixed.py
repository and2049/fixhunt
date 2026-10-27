result = []
for i in range(2):
    val = i and not i  # track iteration
    result.append((val, i))
print(result)
