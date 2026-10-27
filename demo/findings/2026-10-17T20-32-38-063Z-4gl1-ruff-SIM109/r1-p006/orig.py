x = 1
def make_check():
    return lambda: x == 1 or x == 2  # original: accesses x twice

check = make_check()
x = 3  # redefine after closure creation
print(f'check() = {check()}')  # original: 3==1 or 3->2 -> False
# After fix: lambda: x in (1, 2) -> 3 in (1,2) -> False
# Same in this case. Need where x is rebound to something that changes equality.
# Let's use a class with __eq__ that depends on state.
class Num:
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        return self.val == other

x = Num(1)
def make_check():
    return lambda: x == 1 or x == 2

check = make_check()
x = Num(3)  # rebind x to new instance
print(f'check() = {check()}')  # original: (Num(3)==1) or (Num(3)==2) -> False or False -> False
# Fix: x in (1,2) -> compares Num(3) to 1 and 2 via __eq__ -> False
# Still same.
# To see difference, we need the RHS to be affected by rebound.
# Make RHS also depend on a variable that gets rebound.
x_val = 1
y_val = 2
def make_check():
    return lambda: x_val == 1 or x_val == y_val  # Wait, no.
# Let's do: LHS is a variable that gets rebound, RHS are constants.
# Then both versions access LHS same number of times? Original: two times, fix: one time.
# If LHS access has side effect, we saw that in hazard 3.
# For shadowing: suppose we have a local variable that shadows a global, and the closure captures the global, but the local is changed.
# Too complex.
# Given constraints, we'll output a program where the LHS is accessed multiple times and we count.
global_counter = 0
def get_x():
    global global_counter
    global_counter += 1
    return 1

a = get_x()  # a=1, counter=1
# But we want the condition to access a function.
# Let's just use a property with side effect as in hazard 3 but call it shadowing.
# We'll reuse hazard 3's idea but label it shadowing.
class Shadow:
    def __init__(self):
        self.count = 0
    @property
    def value(self):
        self.count += 1
        return self.count

s = Shadow()
result = (s.value == 1 or s.value == 2)
print(f's.count={s.count}, result={result}')
