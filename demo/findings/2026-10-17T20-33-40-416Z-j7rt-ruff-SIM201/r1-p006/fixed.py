side = []
def f():
    side.append('f')
    return 1
def g():
    side.append('g')
    return 2
if not f() == g():   # Triggers SIM201: left-to-right eval of f() then g(), then ==, then not
    print('taken')
print(side)  # Before fix: ['f', 'g']; after fix: same? Actually '!=' also evaluates left then right.
# But SIM201 assumes same order — however, if macros or lazy eval were involved, diff might appear.
# Here we rely on fact that both orders are same, so to show hazard we need divergence.
# Let's instead make one expression have side effect that affects the other.
# Redo:
