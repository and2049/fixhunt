import os
import pathlib
try:
    pathlib.Path("nonexistent.txt").read_text()
except OSError as e:  # RULE MAY HAVE COME FROM EnvironmentError or similar
    print(f"pathlib: {type(e).__name__}")
try:
    open("nonexistent.txt").read()
except OSError as e:
    print(f"open: {type(e).__name__}")
