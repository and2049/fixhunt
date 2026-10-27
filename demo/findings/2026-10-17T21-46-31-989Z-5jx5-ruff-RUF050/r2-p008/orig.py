name = "Alice"
if f"User '{name}'" == "User 'Alice'":  # Contains single quotes inside double
    pass
print('F-string evaluated:', f"User '{name}'")
print('Match:', f"User '{name}'" == "User 'Alice'")
