msg = 'start'
# ruff: ignore[unused-import ]  # Note: \u00A0 is NO-BREAK SPACE after F401
if msg:
    print(msg)
# After fix, if NBSP is stripped, the comment becomes '# ruff: ignore[unused-import]' 
# We detect if the NBSP is preserved by checking the raw byte representation of the comment.
# We print a trace that depends on whether the NBSP is still present.
