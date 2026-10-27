S = {1}
S = {2}
print('start:', S)
for x in S:
    S.add(99)
    break
print('end:', sorted(S))
