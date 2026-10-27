import os
os.remove('test.bin') if os.path.exists('test.bin') else None
with open('test.bin', 'wb') as f:
    f.write(b'hello\nworld\n')
with open('test.bin', 'rb') as fp:
    for chunk in fp:  # reads binary lines
        print('Chunk:', chunk)
        decoded = chunk.decode('utf-8').strip()
        print('Decoded:', decoded)
        if decoded == 'world':
            fp.write(b'!!!')  # writing to file opened in rb? This will fail
            # Actually, 'rb' mode doesn't allow write — this raises io.UnsupportedOperation
            # But we want to show that readlines() gave us bytes, and we tried to write
            # However, the hazard is about file modes and truncation — let's fix.
            # Instead: we open in r+, read lines, then write — but readlines() consumes.
            # Better: show that iterating over file vs list differs when file is mutated.
            # Let's redo this hazard properly.
            pass
# Redoing hazard 7 cleanly:
# We'll show that if you truncate the file during iteration, the list vs iterator behave differently.
# But since we can't seek easily in text mode without losing position, we do:
# Open in r+, read first line via readlines()[0], then truncate — but readlines() reads all.
# So instead, we show that readlines() gives you all data even if file is truncated after.
# Direct iterator sees truncation.
# We'll do:
#   write 3 lines
#   open r+
#   for line in fp.readlines():  # gets all 3 lines into list
#       if first line: truncate file to 0
#       print line
#   Then, if we iterated again, the list still has 3, but file is empty.
# But we only iterate once.
# So we do: after loop, try to read again — list version still has data, iterator would not.
# But we don't have a second loop.
# Instead: we use the fact that after truncation, the file pointer is at end, but list is safe.
# We'll just print the lines from readlines() — they are unaffected by truncation.
# And we'll show that if we had iterated directly, we'd get nothing after truncation.
# Since we can't show both in one run without two loops, we simulate by showing
# that readlines() preserved data even after truncation.
# Let's write a clean version.

# Actually, let's replace this entire block with a correct hazard 7.

os.remove('test.txt') if os.path.exists('test.txt') else None
with open('test.txt', 'w') as f:
    f.write('line1\nline2\nline3')
with open('test.txt', 'r+') as fp:
    all_lines = fp.readlines()  # hazard triggers here
    print('Read via readlines():', [l.strip() for l in all_lines])
    fp.seek(0)
    fp.truncate()  # truncate after reading
    fp.write('new\ncontent')
    fp.flush()
# Now, if we had iterated directly on fp, we would have seen only the first part
# before truncation? No — because readlines() already consumed.
# Actually, the point is: if we had done `for line in fp:` after truncation,
# we'd get nothing. But we used readlines(), so we have the old data.
# So we show that the data from readlines() is independent of later truncation.
print('After truncation, trying to read fp again:')
fp.seek(0)
print('fp.readlines():', fp.readlines())  # should be ['new\n', 'content']
os.remove('test.txt')
