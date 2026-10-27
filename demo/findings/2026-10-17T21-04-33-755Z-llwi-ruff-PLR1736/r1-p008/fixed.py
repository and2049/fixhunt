class Truthy:
    def __init__(self, flag): self.flag = flag
    def __bool__(self):
        print(f'__bool__ called, returning {self.flag}')
        return self.flag

data = [Truthy(True), Truthy(False)]
for n, v in enumerate(data):
    # Rule triggers on data[n] if v > 0 else 0 -> but v is Truthy, not int! Adjusting to match pattern: use v in bool context
    # Instead: data[n] is used in conditional
    if v:  # Rule should trigger here? No — rule only triggers on direct indexing like lst[i], not in if
        # So we need to match the hazard pattern: for n, v in enumerate(nums): nums[n] if v > 0 else 0
        # Let's change to: nums[n] is used in expression
        pass
# Redo to match exact pattern: for n, v in enumerate(nums): nums[n] if v > 0 else 0
# But v is Truthy, not comparable to int. So make v int, but data[n] has side effect
class NumWithBool:
    def __init__(self, val): self.val = val
    def __bool__(self):
        print(f'__bool__({self.val})')
        return self.val != 0
    def __int__(self): return self.val

nums = [NumWithBool(1), NumWithBool(0)]
for n, v in enumerate(nums):
    # Rule triggers on nums[n] -> should become v
    result = v if v > 0 else 0  # Here, nums[n] is indexed, v is loop var
    print(f'n={n}, v={v}, result={result}')
