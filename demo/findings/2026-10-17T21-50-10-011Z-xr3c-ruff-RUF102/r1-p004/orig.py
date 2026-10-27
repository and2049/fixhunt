flag = 0  # noqa: FAKE
if flag:  # this line would be checked if tool behaved strangely
    print('unreachable')
else:
    print(flag)
