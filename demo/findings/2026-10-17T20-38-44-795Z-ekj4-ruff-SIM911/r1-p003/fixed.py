d = {'a': 1, 'b': 2}
# This comment should stay
result = list(zip(d.keys()  # keys comment
                 , d.values()))  # values comment
print('Result:', result)
# After fix, comments may be lost
print('Expected:', list(d.items()))
