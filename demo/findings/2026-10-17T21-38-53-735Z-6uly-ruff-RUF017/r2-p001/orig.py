from __future__ import annotations

def process_lists(lists):
    return sum(lists, [])  # flatten list of int pairs

pairs: list[tuple[int, int]] = [(1, 2), (3, 4)]
result = process_lists(pairs)
print(result)
