"""
@File    :   binary_search_tree.py
@Time    :   2024/8/19 11:47
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
from typing import Optional, List

import parso.tree


class TreeNode:
    def __init__(self, value: int):
        self.val: int = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.parent: Optional['TreeNode'] = None


class BinarySearchTree:

    def __init__(self, val_list: List[int] = []):
        self.root: Optional['TreeNode'] = None
        for n in val_list:
            self.insert(n)

    def insert(self, data: int) -> bool:
        if not self.root:
            self.root = TreeNode(data)
            return True
        else:
            p = None
            n = self.root
            while n:
                if data == n.val:
                    return False
                p = n
                if data < n.val:
                    n = n.left
                else:
                    n = n.right
            new_node = TreeNode(data)
            new_node.parent = p
            if data < p.val:
                p.left = new_node
            else:
                p.right = new_node
        return True

    def insert2(self, data: int) -> bool:
        if not self.root:
            self.root = TreeNode(data)
            return True
        else:
            n = self.root
            while True:
                # 检查是否已经存在相同的值
                if data == n.val:
                    return False
                elif data < n.val:
                    if n.left is None:
                        n.left = TreeNode(data)
                        n.left.parent = n
                        return True
                    n = n.left
                else:
                    if n.right is None:
                        n.right = TreeNode(data)
                        n.right.parent = n
                        return True
                    n = n.right

    def search(self, data: int) -> List[TreeNode]:
        res = []
        n = self.root
        while n:
            if data < n.val:
                n = n.left
            else:
                if data == n.val:
                    res.append(n)
                n = n.right
        return res

    def delete(self, data: int):
        del_list = self.search(data)
        for n in del_list:
            if n.parent is None and n != self.root:
                continue
            else:
                self._del(n)

    def _del(self, node: TreeNode):
        if not node.left and not node.right:
            if node == self.root:
                self.root = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = None
                else:
                    node.parent.right = None
                node.parent = None

        elif node.left is not None and node.right is None:
            if node == self.root:
                self.root = node.left
                self.root.parent = None
                node.left = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

                node.left.parent = node.parent
                node.parent = None
                node.left = None
        elif node.left is None and node.right is not None:
            if node == self.root:
                self.root = node.right
                self.root.parent = None
                node.right = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right

                node.right.parent = node.parent
                node.parent = None
                node.right = None
        else:
