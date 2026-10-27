lst = [1, 2]
s = {1, 2, 3}
try:
    if lst in s:
        s.remove(lst)
except TypeError as e:
    print('remove TypeError:', type(e).__name__, ':', e)
try:
    if lst in s:
        s.discard(lst)
except TypeError as e:
    print('discard TypeError:', type(e).__name__, ':', e)
# Note: In practice, both give same error, but we show the pattern
# Let's make a case where the error might differ in custom class
class Unhashable:
    def __eq__(self, other):
        return True
    def __hash__(self):
        raise TypeError('unhashable')
u = Unhashable()
s2 = {1, 2, 3}
try:
    if u in s2:
        s2.remove(u)
except TypeError as e:
    print('Custom unhashable remove:', type(e).__name__, ':', e)
try:
    if u in s2:
        s2.discard(u)
except TypeError as e:
    print('Custom unhashable discard:', type(e).__name__, ':', e)
