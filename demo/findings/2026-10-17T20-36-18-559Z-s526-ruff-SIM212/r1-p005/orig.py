# This comment should be preserved if possible
val = 'keep'  # inline comment
flag = False
# Rule fires on: val if not flag else 'drop'
result = val if not flag else 'drop'  # keep this comment
print(f'result={result}')
