"""
This module tests quote removal next to docstring.
"""
class Node:
    """A node that references itself via forward ref."""
    parent: "Node" = None
    def walk(self):
        p = self.parent
        print(p.__class__.__name__ if p else 'None')
Node().walk()
