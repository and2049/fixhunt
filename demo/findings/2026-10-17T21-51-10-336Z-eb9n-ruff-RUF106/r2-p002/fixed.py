DEBUG = True
# ruff: ignore[unused-import] if DEBUG
import os  # This should be ignored only if DEBUG is True
if not DEBUG:
    print(os.path)  # This line should cause F401 if suppression failed
else:
    print('suppression active')
