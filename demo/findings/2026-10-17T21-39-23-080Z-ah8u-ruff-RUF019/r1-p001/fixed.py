d = {}
try:
    if d.get("x"):
        print("inside")
except KeyError as e:
    print(f"KeyError: {e}")
print("done")
