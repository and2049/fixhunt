s = 'hello'
print(f'{s} in ["hello", "world"]')  # Not a real membership test
print('%s in ["hello", "world"]' % s)  # Same
print('{s} in ["hello", "world"]'.format(s=s))  # Same
