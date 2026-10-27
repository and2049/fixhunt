# Custom plugin might interpret plain '# ruff: disable' as enabling strict mode
# After fix, becomes '# ruff: disable[]' which plugin may ignore
mode = 'lax'
try:
    exec("# ruff: disable\nif 1: mode = 'strict'")
except:
    pass
print(f"Mode: {mode}")
