d = {'name': 'Alice', 'age': 30}
template = "Hello {name}, you are {age} years old"
if 'name' in d.keys():
    result = template.format(**d)
else:
    result = 'missing'
print(result)
# Also test f-string interaction
if 'age' in d.keys():
    print(f"Age: {d['age']}")
