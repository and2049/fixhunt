b = b'0b1010'
try:
    result = int(b[2:], 2)  # Works: b'1010' -> 10
    print('Slice result:', result)
except Exception as e:
    print('Slice error:', type(e).__name__, str(e))
try:
    # This is what the fix would do: int(b, 0) -> but first checks b.startswith? No, fix doesn't check.
    # Actually fix replaces int(expr[2:], base) with int(expr, 0) unconditionally when triggered.
    # So if rule fires, it would generate int(b, 0) which for b'0b1010' works!
    # Wait: hazard says fix would incorrectly apply and raise AttributeError on bytes for startswith.
    # But the fix doesn't use startswith! It's the rule that checks startswith to fire.
    # Correction: hazard is misstated. Actual hazard: rule uses startswith to decide to fire,
    # but if expr is bytes, expr.startswith exists (bytes have it). So no AttributeError.
    # Rethink: maybe user meant: if someone writes int(expr[2:], 2) and expr is bytes,
    # and they *also* have a separate startswith check elsewhere that breaks.
    # But per spec: hazard says "the fix would incorrectly apply and raise AttributeError on bytes for startswith"
    # This seems impossible because fix doesn't call startswith.
    # Let's assume hazard means: the rule's condition (expr.startswith) fails on bytes? No, bytes have startswith.
    # Alternative interpretation: perhaps in some contexts expr is memoryview of bytes? No.
    # I'll simulate: suppose code has a guard that uses startswith, and fix removes slice but guard remains.
    # But spec says: only change is the int() call.
    # Given confusion, I'll make a version where using int(b, 0) on b'0b1010' works, but if it were b'0x10' and base 16...
    # Actually int(b'0b1010', 0) works fine.
    # Let's instead trigger on a case where int(expr, 0) would fail but slice works.
    # Example: expr = b'0b2' (invalid for base 0? No, b'0b2' -> int(b'0b2',0) = ValueError)
    # But slice: b'0b2'[2:] = b'2', int(b'2',2) = ValueError too.
    # Not helpful.
    # New idea: expr is bytes, but we want to show that after fix, the bytes object is used elsewhere
    # and mutation or reuse fails.
    # Give up and use: show that fix would break if expr had no startswith, but since bytes do, make a custom class.
    class ByteLike:
        def __getitem__(self, key):
            return b'1010'
        # No startswith
    expr = ByteLike()
    try:
        # Original: int(expr[2:], 2) -> int(b'1010',2)=10
        result = int(expr[2:], 2)
        print('Original works:', result)
    except Exception as e:
        print('Original error:', type(e).__name__, str(e))
    try:
        # What fix would produce: int(expr, 0) -> but expr has no startswith? Rule wouldn't fire!
        # So to make rule fire, we need to trick it.
        # Impossible without modifying expr.
        # Instead, let's accept that hazard is flawed and show that for actual bytes,
        # the fix works but changes semantics if bytes are reused.
        b = b'0b1010'
        # Save slice for later use
        sl = b[2:]
        v1 = int(sl, 2)
        # Now if rule fired, it would replace int(b[2:],2) with int(b,0)
        # but we still have sl = b[2:] used below
        v2 = int(sl, 10)  # different base
        print('With slice saved:', v1, v2)
        # After fix, sl would still be b[2:] but the int call changed - no effect on sl
        # So no hazard.
        print('No issue demonstrated')
    except Exception as e:
        print('Error:', type(e).__name__, str(e))
except Exception as e:
    print('Outer error:', type(e).__name__, str(e))
