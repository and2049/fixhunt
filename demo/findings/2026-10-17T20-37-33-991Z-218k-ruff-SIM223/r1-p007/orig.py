from pathlib import Path
p = Path('.')
# Create a temporary file
tmp = Path('tmp.txt')
tmp.write_text('test')
try:
    # Rule triggers on: p and []
    result = p and []
    print('result:', result)
    # Original: p is truthy (Path('.') exists) -> evaluate [] -> returns []
    # Fix: p and [] -> same
    # Now make p falsey? Path objects are truthy even if empty? Actually, Path is always truthy.
    # Instead, use a falsey literal at start
    result2 = [] and p
    print('result2:', result2)
    # Original: [] -> falsey -> returns []
    # Fix: becomes []
    # Same
finally:
    if tmp.exists():
        tmp.unlink()
