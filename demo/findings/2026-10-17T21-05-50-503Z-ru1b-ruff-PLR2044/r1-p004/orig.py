from typing import List, Optional
Node = Optional['Node']  # 
def walk(n: Node) -> List[int]:
    return [] if n is None else [n.val] + walk(n.left) + walk(n.right)
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
try:
    root = Node(1, Node(2), Node(3))
    print(walk(root))
except Exception as e:
    print(type(e).__name__, str(e))
