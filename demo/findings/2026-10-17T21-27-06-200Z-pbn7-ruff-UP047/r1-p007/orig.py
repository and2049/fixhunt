from typing import TypeVar
T = TypeVar('T')
class Tracking:
    access_count = 0
    def __init__(self, value): self._value = value
    @property
    def value(self) -> T:
        Tracking.access_count += 1
        return self._value
obj = Tracking("hello")
print(f"First access: {obj.value}, Count: {Tracking.access_count}")
print(f"Second access: {obj.value}, Count: {Tracking.access_count}")
