with open('temp.txt', 'w') as f:
    f.write('a\nb\nc\n')
# Now read: file object is iterator over lines
with open('temp.txt') as f:
    # Original: list(f) -> ['a\n','b\n','c\n'], [0] -> 'a\n', f exhausted
    lines = list(f)  # Not a trigger: we store it
    first_old = lines[0]
    print('old first:', repr(first_old))
    print('old rest:', [repr(l) for l in lines[1:]])
# Reset: new file
with open('temp.txt') as f:
    # Rewrite trigger: list(f)[0] -> builds list, takes first, f exhausted
    first_new = list(f)[0]  # TRIGGER
    print('new first:', repr(first_new))
    print('new rest attempt:', [repr(l) for l in f])  # f is exhausted -> []
# Rule triggers: on list(f)[0] inside second with block
