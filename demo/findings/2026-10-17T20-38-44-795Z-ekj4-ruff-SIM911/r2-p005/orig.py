from typing import Dict, Any
D: Dict[str, int] = {'a': 1}
ann = D.__annotations__ if hasattr(D, '__annotations__') else {}
k, v = zip(D.keys(), D.values())
print(list(k), list(v), ann)
