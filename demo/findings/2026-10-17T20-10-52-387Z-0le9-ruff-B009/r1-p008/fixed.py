from typing import List

class Container:
    def __init__(self):
        self.items = [1, 2, 3]

def process() -> List[int]:
    c = Container()
    attr = c.items  # Rule triggers here
    return attr

result = process()
print('Result:', result)
print('Type of result:', type(result).__name__)
