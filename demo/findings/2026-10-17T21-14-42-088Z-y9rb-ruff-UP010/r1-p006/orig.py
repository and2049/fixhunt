from __future__ import annotations

class WriteOnly:
    def write(self, data):
        print(f'WriteOnly.write: {data}')
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # No close()

with WriteOnly() as w:
    w.write('hello')
    # The __future__ import above ensures annotations are enabled
    # If removed, and we had type hints relying on it, this could break
    # But here we just print to show flow
print('Context manager done')
