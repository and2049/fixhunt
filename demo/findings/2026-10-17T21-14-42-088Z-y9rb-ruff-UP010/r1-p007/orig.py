from __future__ import annotations \
; print('line continuation used for multi-statement')  # \) is part of import line

# If rule removes the import line, it removes the \ too,
# leaving:
# ; print('line continuation used for multi-statement')
# Which is invalid syntax (leading semicolon)
# But we guard against actual syntax error by making it conditional
# However, to show hazard: we simulate what happens if line is removed
# We can't actually remove it and run, so we show intent via comment
# Instead, we make the import line's presence affect a variable via side effect
import sys
if hasattr(sys, 'flags'):
    print(f'Python flags: {sys.flags}')
else:
    print('No sys.flags')
print('Import line processed')
