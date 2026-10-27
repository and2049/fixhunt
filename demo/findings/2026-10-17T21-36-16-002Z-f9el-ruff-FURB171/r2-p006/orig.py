class BadEq:
    def __eq__(self, other):
        print('__eq__ called')
        return True
obj = BadEq()
x = obj
if x in [obj]:  # True by identity; __eq__ not called
    print('in: yes')
else:
    print('in: no')
if x == obj:  # Calls __eq__ → prints
    print('eq: yes')
else:
    print('eq: no')
