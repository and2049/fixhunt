# This line has a suppression followed by a TODO marker that should persist
# But if the fix deletes 'TODO', the logic changes
value = 42  # ruff: disable TODO
if 'TODO' in __import__('inspect').getsource(lambda: value):
    print('TODO preserved')
else:
    print('TODO deleted - semantics altered')
