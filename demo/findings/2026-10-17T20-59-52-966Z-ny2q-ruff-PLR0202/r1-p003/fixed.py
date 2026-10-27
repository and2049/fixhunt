class C:
    @classmethod
    def m(cls): return cls.__name__
    fs = [(lambda: m()) for _ in range(1)]

print('fs[0]():', fs[0]())  # Should be 'C'
# After fix: if m is descriptor at lambda definition, still works
# But hazard: if class var lookup changes due to timing
