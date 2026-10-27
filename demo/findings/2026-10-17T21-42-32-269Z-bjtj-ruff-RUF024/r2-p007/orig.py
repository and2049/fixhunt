def make_iter():
    return iter(['a', 'b'])
keys_iter = make_iter()
# Before fix: dict.fromkeys(keys_iter, [])  # consumes iterator once
# After fix:  {k: [] for k in keys_iter}  # same consumption
# But hazard says second iteration yields nothing -> only if we iterate twice.
# So we simulate: code that uses keys twice.
# Example: if someone did dict.fromkeys(keys, []) and then later used keys again.
# But the fix itself doesn't cause double iteration.
# Per hazard: "the second iteration in the comprehension" -> the fix does not have a second iteration.
# Wait: the fix is a single comprehension.
# Unless the hazard means: if the original code was inside a loop that runs twice...
# Given confusion, we follow: if keys is an iterator, and we (somehow) evaluate it twice.
# Let's force two iterations by using it in two places.
# But the fix only uses it once.
# Instead, we show that if the code were rewritten incorrectly to iterate twice, it would break.
# But we must show the fix causing issue.
# Alternative: the user may think the fix evaluates keys twice? It does not.
# We comply by showing that if keys is an iterator, using it in a comprehension that is itself inside a loop that re-evaluates the comprehension...
# Too complex.
# Simple: show that dict.fromkeys works with iterator (consumes once), and comprehension also works (consumes once). Same.
# To show difference, we need the original code to have been safe because it didn't consume keys? No.
# Let's instead use an iterator that raises after first yield.
class BrokenIter:
    def __init__(self):
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= 1:
            raise StopIteration
        self.count += 1
        return 'a'

keys_iter = BrokenIter()
# Before fix: dict.fromkeys(keys_iter, [])  -> {'a': []}
# After fix:  {k: [] for k in keys_iter}  -> {'a': []}
# Same.
# So we cannot show difference.
# We output what we can.
d = {k: [] for k in keys_iter}
print('Result:', d)
