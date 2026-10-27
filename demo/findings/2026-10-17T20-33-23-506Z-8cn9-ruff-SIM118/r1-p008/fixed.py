d = {'name': 'Alice', 'age': 30}
template = "Hello {name}, you are {age} years old"
if 'name' in d:
    result = template.format(**d)
else:
    result = 'missing'
print(result)
# Also test f-string interaction
if 'age' in d:
    print(f"Age: {d['age']}")
