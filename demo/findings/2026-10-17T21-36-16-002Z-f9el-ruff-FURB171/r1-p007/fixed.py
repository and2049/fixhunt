class A:
    x = 1
    @property
    def y(self):
        print('GET_Y')
        return 2
a = A()
# Rule triggers: check if a.y in [a.y]
# First, evaluate a.y -> prints GET_Y, returns 2
# Then, check 2 in [a.y] -> evaluates a.y again -> prints GET_Y again, returns 2
# Then 2 in [2] -> True
# So two GET_Y prints
# After fix: a.y == [a.y][0]
# Evaluate [a.y][0]: first a.y -> prints GET_Y, returns 2; builds [2]; [2][0] -> 2
# Then a.y == 2 -> evaluates a.y -> prints GET_Y, returns 2; 2==2 -> True
# So three GET_Y prints
# Thus side effect count differs.
get_y_count = 0
class A2:
    x = 1
    @property
    def y(self):
        nonlocal get_y_count
        get_y_count += 1
        print(f'GET_Y #{get_y_count}')
        return 2
a2 = A2()
get_y_count = 0
print('Testing a2.y in [a2.y]:')
res1 = a2.y in [a2.y]
print(f'Result: {res1}')
print(f'Total GET_Y calls: {get_y_count}')
get_y_count = 0
print('Testing a2.y == [a2.y][0]:')
res2 = a2.y == [a2.y][0]
print(f'Result: {res2}')
print(f'Total GET_Y calls: {get_y_count}')
# Expected: first test: 2 calls; second test: 3 calls
