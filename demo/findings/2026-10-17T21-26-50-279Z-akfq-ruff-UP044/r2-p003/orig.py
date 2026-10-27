import os
try:
    open('missing.txt').close()
except FileNotFoundError as e:
    print(e)
