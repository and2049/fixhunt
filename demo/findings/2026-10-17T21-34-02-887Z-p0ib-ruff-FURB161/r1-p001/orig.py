def f():
    return 3.14
try:
    result = bin(f()).count('1')
except Exception as e:
    print(type(e).__name__, str(e))
try:
    result = f().bit_count()
except Exception as e:
    print(type(e).__name__, str(e))
