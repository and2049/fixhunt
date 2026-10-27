from __future__ import annotations
import os
import pathlib

# Create a temporary file
open('temp.txt', 'w').close()

# Use pathlib and os.path to show potential divergence if annotations affect type inference
# (though they don't directly, we simulate reliance via type-hinted function)
def get_path(p: str) -> pathlib.Path:  # Annotation relies on __future__
    return pathlib.Path(p)

def get_os_path(p: str) -> str:
    return os.path.abspath(p)

p1 = get_path('temp.txt')
p2 = get_os_path('temp.txt')
print(f'pathlib: {p1.resolve()}')
print(f'os.path: {p2}')

# Clean up
os.remove('temp.txt')
print('Cleanup done')
