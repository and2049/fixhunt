class EmptyButTrue:
    def __len__(self):
        return 0
    def __bool__(self):
        return True
x = EmptyButTrue()
if x in [x]:  # Identity → True
    print('in: True')
else:
    print('in: False')
if x == x:  # True (default __eq__ is identity)
    print('eq: True')
else:
    print('eq: False')
