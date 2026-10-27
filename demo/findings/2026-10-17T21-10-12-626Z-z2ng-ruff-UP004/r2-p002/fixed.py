from typing import List

class Parser:
    def parse(self, data: List[int]) -> List[str]:
        return [str(x) for x in data]

p = Parser()
result = p.parse([1, 2, 3])
print(result)
