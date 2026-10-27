data = [('a', 1), ('b', 1), ('c', 2)]
result_before = list(reversed(sorted(data, key=lambda x: x[1])))
sorted_direct = sorted(data, key=lambda x: x[1], reverse=True)
print('Before fix:', result_before)
print('After fix :', sorted_direct)
print('Equal?', result_before == sorted_direct)
