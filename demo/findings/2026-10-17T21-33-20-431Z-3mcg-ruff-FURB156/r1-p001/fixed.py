import string
s = string.digits
t = string.digits
print(s is t)
s_replaced = string.digits  # This line triggers FURB156
t_replaced = string.digits
print(s_replaced is t_replaced)
