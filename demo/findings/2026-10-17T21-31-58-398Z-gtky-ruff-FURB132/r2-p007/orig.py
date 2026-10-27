remove = lambda x: print('shadowed remove called with', x)
discard = lambda x: print('shadowed discard called with', x)
s = {1, 2, 3}
x = 2
if x in s:
    remove(x)  # This calls the shadowed remove, not set.remove
print('After shadowed remove, s unchanged:', s)
# Now if we had used discard via fix, it would call shadowed discard
# But to show the hazard, we demonstrate what the fix would change
# Reset and show what happens with real methods
 del remove, discard  # remove shadowing
if x in s:
    s.remove(x)  # real set.remove
print('After real remove:', s)
s.add(x)  # add back
if x in s:
    s.discard(x)  # real set.discard
print('After real discard:', s)
