# Configuration	with mixed	whitespace  # ruff: ignore[trailing-whitespace]
value = 42
# After rewrite, comment still has \t but linters may warn
print(value)
