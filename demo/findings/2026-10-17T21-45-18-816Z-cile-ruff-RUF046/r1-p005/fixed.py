# This line's length affects flake8 or black line length scoring
val = 5 + 3  # kept for formatting
print('Value:', val)
# If removed: 'val = 5 + 3' is shorter; tools may reformat differently
# We show the line length as proxy
import inspect
import textwrap
src = inspect.getsource(lambda: (5 + 3))
print('Source length of int(5+3):', len(src.strip()))
