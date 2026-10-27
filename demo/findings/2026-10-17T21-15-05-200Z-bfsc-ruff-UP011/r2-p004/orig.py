from __future__ import annotations
import functools
@functools.lru_cache()
def process_data(value: 'DataProcessor') -> int:
    return len(str(value))
class DataProcessor:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return str(self.data)
dp = DataProcessor('test123')
print(process_data(dp))
print(process_data(dp))  # Should be cached
