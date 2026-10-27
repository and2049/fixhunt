calls = []
def get_dict():
    calls.append(len(calls))
    return {'x': 1, 'y': 2}
k, v = zip(get_dict().keys(), get_dict().values())
print(list(k), list(v), calls)
