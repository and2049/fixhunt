x = "hello"
x = "prefix-" + x
print('result:', x)
# Rule does not fire: target x is not LHS of BinOp RHS
