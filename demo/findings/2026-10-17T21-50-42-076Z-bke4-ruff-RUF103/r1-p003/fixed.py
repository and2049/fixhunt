# Tool checks for '# ruff: disable' to enable verbose logging
# Fix changes it to '# ruff: disable[]' which tool ignores
verbose = False
if '# ruff: disable' in open(__file__).read():
    verbose = True
print(f"Verbose logging: {verbose}")
