with open('test.txt', 'w') as f:
    f.write(b'hello')  # Writing bytes to text-mode file → raises TypeError
    if f is not None:  # Trigger: compares file object to None
        print('file open')
    else:
        print('file closed')
# After fix: `f != None` → still safe? But wait — the write fails earlier.
# Let's move the check before write to isolate.
# Rewriting...
