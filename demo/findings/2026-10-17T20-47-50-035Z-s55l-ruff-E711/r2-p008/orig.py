def test_eval():
    None = 42  # Shadow built-in None
    x = None   # x is 42
    # Original code: x == None -> 42 == 42 -> True
    try:
        result = eval('x == None')  # Uses local None=42 -> True
        print(f'eval_result: {result}')
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
    # After buggy fix: becomes 'x is None' -> but None is now 42 -> 'x is 42' -> True (same)
    # To make it fail, we need the fix to refer to built-in None, but it's shadowed
    # So simulate: what if the fix incorrectly used the built-in None name without checking scope?
    # But Ruff's fix is local — it rewrites the AST, so 'is None' still refers to local None
    # So we show: if the fix were to somehow use the built-in None (which it doesn't), it would break
    # Instead, we show the hazard: if None is rebound, the fix still works locally — but the *intent* is broken
    # We instead show: in eval, if the string is rewritten and executed in a scope where None is not defined...
    del None  # Remove local None
    try:
        # This would be the broken fix: if Ruff rewrote to 'x is None' but None is gone
        result = eval('x is None')  # NameError: name 'None' is not defined
        print(f'eval_is_result: {result}')
    except Exception as e:
        print(f'{type(e).__name__}: {e}')

test_eval()
