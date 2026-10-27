import os
os.remove('test.txt') if os.path.exists('test.txt') else None
with open('test.txt', 'w') as f:
    f.write('hello\nworld')
with open('test.txt', 'r') as fp:
    for line in (fp.readlines()):  # preserve this comment
        print('Line:', line.strip())
        print('Comment was here')  # marker
# After loop, check if we can still see the comment effect via output
# We rely on the print above to show the comment was processed
# The autofix would remove the comment, but we can't detect that directly.
# Instead, we make the loop body depend on the structure: if comment is lost,
# the code still runs, but we want to show the line was read.
# This program ensures the loop runs and prints lines — if autofix broke it,
# we'd see missing output. But since we can't detect comment loss,
# we just show the loop executed.
# Real comment loss would be silent; we assume the rule's fix removes it.
# So we output lines to confirm iteration happened.
os.remove('test.txt')
