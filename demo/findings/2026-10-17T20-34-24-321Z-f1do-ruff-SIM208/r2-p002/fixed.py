lst = [1]  # length 1
idx_list = []
def get_idx():
    idx_list.append(0)
    val = len(idx_list)
    lst.clear()
    return val
try:
    result = bool(lst[get_idx()])
except IndexError as e:
    passes = len([i for i in range(len(idx_list)) if i < len(lst)])
    print(f'Exception caught: {type(e).__name__}: {e}, index evaluations: {len(idx_list)}')
else:
    print(f'Result: {result}')
