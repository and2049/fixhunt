import ast
code = 'x = 1  # noqa:  E402'
tree = ast.parse(code)
comment = tree.body[0].value.comment if hasattr(tree.body[0].value, 'comment') else None
print(comment is None or 'E402' in str(comment))
