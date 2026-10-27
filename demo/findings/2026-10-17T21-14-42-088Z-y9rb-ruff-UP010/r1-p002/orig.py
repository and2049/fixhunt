# Rule does not trigger on aliased imports
from __future__ import annotations as ann

# If the rule incorrectly fired and removed this, 'ann' would be undefined
try:
    print(f'ann = {ann}')
except NameError as e:
    print(f'NameError: {e}')
