class Falsy:
    def __bool__(self): return False

d = {'x': Falsy()}
if "x" in d and d["x"]:
    print("true")
else:
    print("false")
if d.get("x"):
    print("true after get")
else:
    print("false after get")
