lst = [99]
result_old = list(lst)[0]
lst[0] = 88
result_new = list(lst)[0]
print('old:', result_old)
print('new:', result_new)
# Rule triggers on: list(lst)[0]
