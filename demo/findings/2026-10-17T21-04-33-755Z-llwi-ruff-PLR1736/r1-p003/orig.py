def g(x, lst=[]):
    lst.append(x)
    return lst

data = [1, 2]
results = []
for idx, val in enumerate(data):
    # Rule triggers on data[idx] -> should become val
    results.append(g(val, data))  # Passing data as explicit lst
print('Results:', results)
print('Final data:', data)
