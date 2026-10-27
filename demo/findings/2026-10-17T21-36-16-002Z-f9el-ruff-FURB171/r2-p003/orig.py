x = 'None'
s = f"{None!r}"  # 'None'
if x in s:  # True: 'None' in 'None'
    print('in formatted')
else:
    print('not in formatted')
if x == s:  # False: 'None' == 'None' → True? Wait — fix!
    print('eq')
else:
    print('not eq')
