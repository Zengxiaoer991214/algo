"""
@File    :   binary_search_tree.py
@Time    :   2024/8/19 11:47
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
import math
from queue import Queue
from typing import Optional, List


class TreeNode:
    def __init__(self, value: int):
        self.val: int = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.parent: Optional['TreeNode'] = None


class BinarySearchTree:

    def __init__(self, val_list=None):
        if val_list is None:
            val_list = []
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
            min_node = node.right
            if min_node.left:
                min_node = min_node.left
            if node.val != min_node.val:
                node.val = min_node.val
                self._del(min_node)
            else:
                self._del(min_node)
                self._del(node)

    def get_min(self) -> Optional[int]:
        if self.root is None:
            return None

        n = self.root
        while n.left:
            n = n.left
        return n.val

    def get_max(self) -> Optional[int]:
        if not self.root:
            return None

        n = self.root
        while n.right:
            n = n.right
        return n.val

    def in_order(self) -> List[int]:
        if not self.root:
            return []
        return self._in_order(self.root)

    def _in_order(self, node: TreeNode) -> List[int]:
        if not node:
            return []
        res = []
        n = node
        res.extend(self._in_order(n.left))
        res.append(n.val)
        res.extend(self._in_order(n.right))
        return res

    def __repr__(self):
        print(str(self.in_order()))
        return self._draw_tree()

    def _draw_tree(self) -> str | None:
        nodes = self._bfs()

        if not nodes:
            print('Empty Tree')
            return

        layer_num = int(math.log(nodes[-1][1], 2)) + 1
        prt_nums = []
        for n in range(layer_num):
            prt_nums.append([None] * 2 ** n)

        for v, p in nodes:
            row = int(math.log(p, 2))
            col = p % 2**row
            prt_nums[row][col] = v

        prt_str = ''
        for l in prt_nums:
            prt_str += str(l)[1:-1] + "\n"

        return prt_str

    def _bfs(self):
        if not self.root:
            return []

        res = []
        q = Queue()
        q.put((self.root, 1))
        while not q.empty():
            n = q.get()
            if n[0] is not None:
                res.append((n[0].val, n[1]))
                q.put((n[0].left, n[1] * 2))
                q.put((n[0].right, n[1] * 2 + 1))
        return res


if __name__ == '__main__':
    nums = [4, 2, 5, 6, 1, 7, 3]
    bst = BinarySearchTree(nums)
    print(bst)

    # 插入
    bst.insert(1)
    bst.insert(4)
    print(bst)

    # 搜索
    for n in bst.search(2):
        print(n.parent.val, n.val)

    # 删除
    bst.insert(6)
    bst.insert(7)
    print(bst)
    bst.delete(7)
    print(bst)
    bst.delete(6)
    print(bst)
    bst.delete(4)
    print(bst)

    # min max
    print(bst.get_max())
    print(bst.get_min())
