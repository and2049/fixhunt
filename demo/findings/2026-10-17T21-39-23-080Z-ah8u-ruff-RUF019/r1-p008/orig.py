class Falsy:
    def __bool__(self): return False

d = {'x': Falsy()}
in_check = "x" in d and d["x"]
get_check = d.get("x")
print(f'in_check: {in_check}, get_check: {bool(get_check)}')
if in_check:
    print("original block")
else:
    print("original skip")
if get_check:
    print("fix block")
else:
    print("fix skip")
