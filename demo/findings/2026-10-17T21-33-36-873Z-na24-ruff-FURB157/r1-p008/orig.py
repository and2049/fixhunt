from decimal import Decimal

log = []
def g():
    log.append('g')
    return 42

# Rule target: str(0) in first arg
result = Decimal(str(0)), g(), log
print('log before:', log)
# Access to force eval
_ = result
print('log after:', log)
# If str(0) were removed, g() still runs once, but if code were f(g(), str(0)) and str(0) removed, still runs.
# To show order: make first arg have side effect via str() on var with __str__ side effect
class StrWithSide:
    def __str__(self):
        log.append('strcalled')
        return '0'

log.clear()
s = StrWithSide()
print('Before fix:', log)
v = Decimal(str(s))  # Would trigger if s were int literal, but it's not
print('After str(s):', log)
print('Decimal:', v)
# Now with literal: this is the trigger
log.clear()
v2 = Decimal(str(0))  # Rule target
print('After str(0):', log)
print('Decimal:', v2)
# After fix: becomes Decimal(0), no __str__ call, so log empty
# We simulate by showing what log *would* be if fix removed call
