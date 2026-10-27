template = '%(a)s %(a)s'
data = {'a': 42, 'unused': 'should_not_be_removed_by_rule'}
result = template % data
print('Output:', result)
