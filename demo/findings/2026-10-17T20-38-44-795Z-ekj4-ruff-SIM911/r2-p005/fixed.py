from typing import Dict, Any
D: Dict[str, int] = {'a': 1}
ann = D.__annotations__ if hasattr(D, '__annotations__') else {}
k, v = D.items()
print(list(k), list(v), ann)
