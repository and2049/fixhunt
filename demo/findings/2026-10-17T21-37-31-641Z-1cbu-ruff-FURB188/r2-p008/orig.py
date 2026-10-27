prefix = 'a'
words = ['apple', 'banana', 'avocado']
result = [w[len(prefix):] if w.startswith(prefix) else w for w in prefix := ['a'] * 3][0]
print(result)
