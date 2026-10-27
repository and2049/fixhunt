x = None
print('x == False:', x == False)
print('not x:', not x)
# Show the difference in conditional context
if x == False:
    print('Takes == False branch')
else:
    print('Skips == False branch')
if not x:
    print('Takes not x branch')
else:
    print('Skips not x branch')
