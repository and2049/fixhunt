import ast
tree = ast.parse("u'test'")
unparsed = ast.unparse(tree)
print(unparsed)\
# Before: u'"test"' -> after fix: "test"
# So unparsed loses u-prefix, breaking fidelity
