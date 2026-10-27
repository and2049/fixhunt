x = 2
y = 3
result = x == True and y  # Rule fires
print('Result:', result)  # Prints False
# After rewrite becomes: x and y -> 2 and 3 -> 3
print('Rewritten would be:', x and y)
