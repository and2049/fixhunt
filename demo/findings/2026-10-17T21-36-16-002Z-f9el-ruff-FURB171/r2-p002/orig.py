x = ''
if x in "":  # Rule does NOT fire: string len=0 → skip (but we want trigger)
    print('matched')
else:
    print('not matched')
if x == "":
    print('eq matched')
else:
    print('eq not matched')
