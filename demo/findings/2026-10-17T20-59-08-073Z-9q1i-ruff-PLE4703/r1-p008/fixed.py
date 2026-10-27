s = {1}
def f(x, seen=s):
    seen.add(99)
    return len(seen)
for x in s:
    print(f(x))
    s.clear()
break
