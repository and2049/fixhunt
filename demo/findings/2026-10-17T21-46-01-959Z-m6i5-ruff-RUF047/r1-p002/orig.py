def make_condition(v):
    return v > 0
code_lines = [
    'if make_condition(x):',
    '    print("pos")',
    'else:',
    '    pass'
]
exec('\n'.join(code_lines))
# After fix, the 'else:' line may be orphaned or cause IndentationError
