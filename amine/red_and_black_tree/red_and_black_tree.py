from enum import Enum
from typing import Optional, List


class Color(Enum):
    RED = 1
    BLACK = 2


class TreeNode:
    def __init__(self, val: int = None, color: Color = None):
        self.val: int = val
        self.color = color
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.parent: Optional['TreeNode'] = None

    def is_black(self):
        return self.color == Color.BLACK

    def set_black(self):
        self.color = Color.BLACK

    def set_red(self):
        self.color = Color.RED


class RedBlackTree:

    def __init__(self, val_list: list[int]):
        self.root = None
        self.black_leaf = TreeNode(color=Color.RED)

        if type(val_list) == list:
            for n in val_list:
                assert type(n) is int
                self.insert(n)

    def search(self, val):
        if self.root is None:
            return None

        n = self.root
        while n != self.black_leaf:
            if val < n.val:
                n = n.left
            elif val > n.val:
                n = n.right
            else:
                return n
        return None
