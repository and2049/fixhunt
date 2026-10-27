class A(dict):  # inline comment
    """This is a docstring."""
    def method(self):
        return 'ok'
print('A.__doc__:', A.__doc__)
# Simulate checking comment attachment via AST-like behavior
import ast
tree = ast.parse('''class A(dict):  # inline comment
    \"\"\"This is a docstring.\"\"\"
    def method(self):
        return 'ok' ''')
cls = tree.body[0]
print('has inline comment?', hasattr(cls, 'comment') if hasattr(cls, 'comment') else 'N/A')
print('method result:', A().method())
