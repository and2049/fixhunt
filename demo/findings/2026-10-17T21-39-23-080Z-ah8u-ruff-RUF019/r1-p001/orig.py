d = {}
try:
    if "x" in d and d["x"]:
        print("inside")
except KeyError as e:
    print(f"KeyError: {e}")
print("done")
