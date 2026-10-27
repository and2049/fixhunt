funcs = []
for i in range(3):
    if (val := i) == True:  # Rule fires: val == True
        funcs.append(lambda: val)
    else:
        funcs.append(lambda: -1)
print([f() for f in funcs])  # Prints [0, -1, -1] because only i=0 makes val==True? Wait: i=0 -> val=0 == True? False. i=1 -> val=1 == True -> True. So index 1 captures val=1.
# Correction: i=0: val=0 -> 0==True False -> lambda:-1
# i=1: val=1 -> 1==True True -> lambda: val (which is 1 at definition time, but late binding)
# i=2: val=2 -> False -> -1
# All lambdas capture `val` from enclosing scope, which ends up as 2 after loop.
# So prints [2, 2, 2] if all lambdas are called after loop.
# But we want to see difference after rewrite.
# Let's refactor to make it sensitive.
