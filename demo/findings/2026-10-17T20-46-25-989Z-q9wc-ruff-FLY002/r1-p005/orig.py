s = {'b', 'a'}
joined = ''.join(s)
fstringed = ''.join([f'{c}' for c in s])  # simulate f-string order
print(f'join:{joined}|fstring_sim:{fstringed}')
# To see difference, we need fixed iteration vs random; but sets are unordered.
# Instead show that f-string forces list order while join uses set's arbitrary order.
# We'll run twice and see if join differs.
results = []
for _ in range(2):
    s = {'b', 'a'}
    results.append(''.join(s))
print(f'join varies: {results[0] != results[1]}')
