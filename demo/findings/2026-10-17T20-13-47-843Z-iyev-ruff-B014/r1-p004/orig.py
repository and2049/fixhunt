try:
    1/0
except (ZeroDivisionError, ArithmeticError):
    print('except')
finally:
    print('finally')
