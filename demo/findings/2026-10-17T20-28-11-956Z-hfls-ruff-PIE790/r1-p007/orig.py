for i in range(2):
    if i == 0:
        pass  # Rule triggers: removable pass
        # if False:
        #     break
    else:
        print('else ran')  # Should run only if inner if didn't break
# After fix: inner if has no body -> syntax error? No: pass removed leaves empty if -> IndentationError
# But we want deterministic output: so make it so that without pass, the comment shifts and breaks nesting
# Let's restructure to avoid syntax error but change logic
for i in range(1):
    if i == 0:
        x = 1
        pass  # Rule triggers
        # TODO: handle i==0
    else:
        print('else')
print('done')
