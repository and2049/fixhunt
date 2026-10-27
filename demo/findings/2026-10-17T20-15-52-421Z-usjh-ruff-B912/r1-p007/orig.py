def g(): try: return 1/0
except ZeroDivisionError: return 'inf'
finally: print('finally ran')
def h(x): return g() + x
try:
    list(map(h, [1, 2], [3]))  # triggers strict
    print('completed')
except ValueError as e:
    print('ValueError:', str(e))
