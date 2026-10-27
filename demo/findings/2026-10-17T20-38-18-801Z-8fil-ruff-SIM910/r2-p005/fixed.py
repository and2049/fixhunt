from typing import Dict, Any
def fetch(mapping: Dict[str, Any], key: str) -> Any:
    return mapping.get(key)
d: Dict[str, Any] = {}
result = fetch(d, 'missing')
print('result:', result, 'type:', type(result))
# Rule triggers on mapping.get(key, None) -> removes None
# Same behavior, but shows interaction with typed function
