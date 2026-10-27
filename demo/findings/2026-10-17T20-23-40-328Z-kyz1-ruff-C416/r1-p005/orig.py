data = [1, 2, 3]
result = {x: y for x, y in [(x, x*2) for x in data] if (tmp := x) is not None}
print('result:', result)
try:
    print('tmp:', tmp)
except NameError as e:
    print('tmp not accessible:', type(e).__name__)
