"""
@File    :   binary_search_tree.py
@Time    :   2024/8/20 9:26
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
from typing import Optional


class TreeNode:

    def __init__(self, value: int):
        self.val: int = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class BinarySearchTree:

    def __init__(self):
        self._root = None

    @property
    def root(self) -> Optional[TreeNode]:
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    def find(self, value: int) -> Optional[TreeNode]:
        node = self.root
        while node and node.val != value:
            node = node.left if node.val > value else node.right
        return node

    def insert(self, value: int):
        if not self.root:
            self.root = TreeNode(value)
            return
        parent = None
        node = self.root
        while node:
            parent = node
            node = node.left if node.val > value else node.right
        new_node = TreeNode(value)
        if parent.val > value:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, value: int):
        node = self.root
        parent = None
        while node and node.val != value:
            parent = node
            node = node.left if node.val > value else node.right
        if not node:
            return

        if node.left and node.right:
            successor = node.right
            successor_parent = node
            while successor.left:
                successor_parent = successor
                successor = successor.left
            node.val = successor.val
            parent, node = successor_parent, successor

        child = node.left if node.left else node.right
        if not parent:
            self.root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child
