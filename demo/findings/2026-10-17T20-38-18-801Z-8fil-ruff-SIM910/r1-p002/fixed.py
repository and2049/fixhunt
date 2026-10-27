data = {'x': 10}
result = [(v := data.get(k)) for k in ['x', 'y'] if v is not None]
print(result)
