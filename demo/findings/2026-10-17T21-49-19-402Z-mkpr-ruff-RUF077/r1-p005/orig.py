class C:
    def method(self=42):
        return self * 2

print(C.method())
try:
    C().method()
except Exception as e:
    print(type(e).__name__, str(e))
