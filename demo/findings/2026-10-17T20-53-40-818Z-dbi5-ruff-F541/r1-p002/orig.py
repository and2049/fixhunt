template = f"Hello"
value = template % {}
print(value)
try:
    f"{template}"
except Exception as e:
    print(type(e).__name__, str(e))
