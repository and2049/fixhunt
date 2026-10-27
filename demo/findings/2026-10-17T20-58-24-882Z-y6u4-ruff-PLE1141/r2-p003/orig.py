d = {(1, 2): 'found', (3, 4): 'lost'}
print('Original:')
for k, v in d:  # Rule fires: unpacks tuple key into k,v
    print(f'k={k}, v={v}')
print()
print('Expected after .items():')
for item in d.items():
    print(f'item={item}')
