class BadEq:
    def __eq__(self, other):
        raise ValueError('bad eq')
    def __ne__(self, other):
        return False
b = BadEq()
try:
    if not b == b:   # Triggers SIM201
        pass
except ValueError as e:
    print(f'caught: {e}')
# Original: evaluate b==b -> raises ValueError -> 'not' never reached.
# After fix: b != b -> calls __ne__ -> returns False -> no exception.
# So behavior differs: exception vs no exception.
# We catch and print to show difference.
