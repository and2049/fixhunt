# Line 1: suppression
# ruff: disable
# Line 2: this line's number is referenced in debug info
DEBUG_LINE = 2
import inspect
lines = inspect.getsourcelines(lambda: None)[0]
actual_line = lines[DEBUG_LINE - 1].strip() if DEBUG_LINE <= len(lines) else "OUT_OF_RANGE"
print(f"Line {DEBUG_LINE} content: {repr(actual_line)}")
