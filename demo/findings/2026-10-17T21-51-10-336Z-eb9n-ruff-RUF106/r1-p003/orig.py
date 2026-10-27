# Configuration	with mixed	whitespace  # ruff: ignore[W291]
value = 42
# After rewrite, comment still has \t but linters may warn
print(value)
