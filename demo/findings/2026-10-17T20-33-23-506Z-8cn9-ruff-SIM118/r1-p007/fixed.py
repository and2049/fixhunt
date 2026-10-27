lst = [1, 2, 3]
try:
    # This line should NOT trigger SIM118 because lists have no .keys()
    if 'a' in lst.keys():
        pass
except AttributeError as e:
    print(type(e).__name__, str(e))
