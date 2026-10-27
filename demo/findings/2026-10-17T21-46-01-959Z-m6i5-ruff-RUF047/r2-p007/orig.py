if False:
    x = 1
else:
    pass  # important: fallback logic
print(x if 'x' in locals() else 'undefined')
