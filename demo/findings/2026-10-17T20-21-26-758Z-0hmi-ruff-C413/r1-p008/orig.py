ref = []
def side_effect(x):
    ref.append(x)
    return -x
data = [1, 2, 3]
transformed = [side_effect(x) for x in data]
sorted_transformed = sorted(transformed)
list_wrapped = list(sorted_transformed)
print('Side effect log:', ref)
print('List wrapped:', list_wrapped)
print('Sum of wrapped:', sum(list_wrapped))
