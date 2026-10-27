if False:
    from __future__ import annotations  # Rule fires here (even though dead code)

# Even though the import is never executed, removing it changes AST
# Simulate a tool that scans for future imports statically
import ast
with open(__file__, 'r') as f:
    tree = ast.parse(f.read())

future_imports = [n for n in ast.walk(tree) if isinstance(n, ast.ImportFrom) and n.module == '__future__']
print(f'Static future imports found: {len(future_imports)}')

# Runtime behavior unchanged because block never runs
print('Runtime: no future import executed')
