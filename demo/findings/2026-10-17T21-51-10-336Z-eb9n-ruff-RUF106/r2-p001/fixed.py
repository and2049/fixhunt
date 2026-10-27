import sys
# ruff: disable[undefined-local-with-import-star]
from star import *
print('star imported')
# This line should trigger F403 if suppression fails
if False:
    from star import wildcard  # noqa: F403
