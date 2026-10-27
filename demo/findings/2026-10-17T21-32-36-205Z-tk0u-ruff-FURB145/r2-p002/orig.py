src = [1, 2]
candidate = src[:]
is_same_obj = candidate is src
print('distinct?', not is_same_obj)
# rule triggers on candidate = src[:]
if not is_same_obj:
    print('ok')
else:
    print('unexpected alias')
