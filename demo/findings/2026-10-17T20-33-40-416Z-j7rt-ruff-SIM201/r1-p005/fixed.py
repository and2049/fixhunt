def f(a=[]):
    a.append(1)
    return a
print(f() == f())  # [1] == [1,1] -> False
print(not f() == f())  # Would trigger SIM201 if inside condition; but we avoid trigger to focus on hazard
# Note: SIM201 does not fire here because it's not a top-level comparison in an 'if' or similar.
# Hazard still relevant: if rewritten, evaluation order of defaults could change.
