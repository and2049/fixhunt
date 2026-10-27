class Obj:
    def __eq__(self, other):
        print('__eq__ called')
        return True
x = Obj()
if x is not None:
    print('identity')
else:
    print('not identity')
# After fix: `x != None` calls __eq__ → prints '__eq__ called', then evaluates to False → prints 'not identity'
