x = 42
s = f"Value: {x}#"
print(s)
s2 = b"data#"
print(s2)
# Recovery: reset and show correct behavior
x = 42
s = f"Value: {x}#"  # real comment
print(s)
s2 = b"data#"  # real comment
print(s2)
