s = "0123456789"
t = "0123456789"
print(s is t)
s_replaced = "0123456789"  # This line triggers FURB156
t_replaced = "0123456789"
print(s_replaced is t_replaced)
