import queue
from enum import Enum
from queue import Queue
from typing import Optional
import pygraphviz as pgv


class Color(Enum):
    RED = "red"
    BLACK = "black"


class TreeNode:
    def __init__(self, val: int = None, color: Color = None):
        self.val: int = val
        self.color = color
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.parent: Optional['TreeNode'] = None

    def is_black(self) -> bool:
        return self.color == Color.BLACK

    def set_black(self):
        self.color = Color.BLACK

    def set_red(self):
        self.color = Color.RED


class RedBlackTree:

    def __init__(self, val_list: list[int]):
        self.root: Optional[TreeNode] = None
        self.black_leaf = TreeNode(color=Color.BLACK)
        for n in val_list:
            self.insert(n)

    @staticmethod
    def parent(node: TreeNode):
        """
        获取父节点
        :param node:
        :return:
        """
        return None if node is None else node.parent

    @staticmethod
    def bro(node: TreeNode):
        """
        获取兄弟节点
        :param node:
        :return:
        """
        if node is None or node.parent is None:
            return None
        else:
            p = node.parent
            if node == p.left:
                return p.right
            else:
                return p.left

    def search(self, val: int):
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

    def insert(self, val: int):
        new_node = TreeNode(val, Color.RED)

        if self.root is None:
            self.root = new_node
        else:
            n = self.root
            while n != self.black_leaf:
                p = n
                if val < n.val:
                    n = n.left
                elif val > n.val:
                    n = n.right
                else:
                    raise KeyError(f'val:{val} already exists')

            if val < p.val:
                p.left = new_node
            else:
                p.right = new_node
            new_node.parent = p
        new_node.left = new_node.right = self.black_leaf
        self._insert_fixup(new_node)

    def _insert_fixup(self, node: TreeNode):
        n = node
        while n is not self.root and n.parent.is_black():
            # 父p 叔u 祖父g
            p = self.parent(n)
            u = self.bro(p)
            g = self.parent(p)

            if not u.is_black():
                p.set_black()
                u.set_black()
                g.set_red()
                n = g
                continue

            if p == g.left:
                if n == p.right:
                    self.rotate_l(p)
                    n, p = p, n
                p.set_black()
                g.set_red()
                self.rotate_r(g)
            else:
                if n == p.left:
                    self.rotate_r(p)
                    n, p = p, n
                p.set_black()
                g.set_red()
                self.rotate_l(g)

        self.root.color = Color.BLACK

    def rotate_l(self, node: TreeNode):
        if node is None:
            return

        if node.right is self.black_leaf:
            return

        p = self.parent(node)
        x = node
        y = node.right

        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:
            self.root = y

        x.parent, y.parent = y, p

        if y.left != self.black_leaf:
            y.left.parent = x

        x.right, y.left = y.left, x

    def rotate_r(self, node: TreeNode):
        if node is None:
            return

        if node.left is self.black_leaf:
            return

        p = self.parent(node)
        x = node
        y = node.left

        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:
            self.root = y

        x.parent, y.parent = y, p

        if y.right is not None:
            y.right.parent = x
        x.left, y.right = y.right, x

    def delete(self, val: int):
        n = self.search(val)
        if n is None:
            print(f'cannot find the node: {val}')
            return

        self._delete_node(n)

    def _delete_node(self, node: TreeNode):
        n = node

        if self.children_count(n) == 2:
            s = n.right
            while s.left != self.black_leaf:
                s = s.left
            n.val = s.val
            n = s

        if n.left == self.black_leaf:
            c = n.right
        else:
            c = n.left

        self._transplant(n, c)

        if n.is_black():
            self._delete_fixup(c)

    def _delete_fixup(self, node: TreeNode):
        n = node
        while n != self.root and n.is_black():
            p = self.parent(n)
            b = self.bro(n)

            if p.left == n:
                if not b.is_black():
                    b.set_black()
                    p.set_red()
                    self.rotate_l(p)
                    b = self.bro(n)
                if b.left.is_black() and b.right.is_black():
                    b.set_red()
                    n = p
                else:
                    if b.right.is_black():
                        b.left.set_black()
                        b.set_red()
                        self.rotate_r(b)
                        b = self.bro(n)

                    b.color = p.color
                    p.set_black()
                    b.right.set_black()
                    self.rotate_l(p)
                    n = self.root
            else:
                if not b.is_black():
                    b.set_black()
                    p.set_red()
                    self.rotate_r(p)
                    b = self.bro(n)

                if b.left.is_black() and b.right.is_black():
                    b.set_red()
                    n = p
                else:
                    if b.left.is_black():
                        b.right.set_black()
                        b.set_red()
                        self.rotate_l(b)
                        b = self.bro(n)
                    b.color = p.color
                    p.set_black()
                    b.left.set_black()
                    self.rotate_r(p)
                    n = self.root
        n.set_black()

    def children_count(self, node: TreeNode) -> int:
        return 2 - [node.left, node.right].count(self.black_leaf)

    def _transplant(self, n1: TreeNode, n2: TreeNode):
        if n1 == self.root:
            if n2 != self.black_leaf:
                self.root = n2
                n2.parent = None
            else:
                self.root = None
        else:
            p = self.parent(n1)
            if p.left == n1:
                p.left = n2
            else:
                p.right = n2
            n2.parent = p

    def draw_img(self, img_name='Red_Black_Tree'):
        if self.root is None:
            return

        tree = pgv.AGraph(directed=True, strict=True)

        q = Queue[TreeNode]()
        q.put(self.root)
        while not q.empty():
            n = q.get()
            if n != self.black_leaf:
                tree.add_node(n.val, color=n.color.value)
                for c in [n.left, n.right]:
                    q.put(c)
                    color = Color.RED.value if c == n.left else Color.BLACK.value
                    if c != self.black_leaf:
                        tree.add_edge(n.val, c.val, color=color)
                    else:
                        tree.add_edge(n.val, 'None', color=color)

        tree.graph_attr['epsilon'] = '0.01'
        tree.layout('dot')
        tree.draw("C:/" + img_name)
        return True


if __name__ == '__main__':
    rbt = RedBlackTree()

    # insert
    nums = list(range(1, 25))
    # random.shuffle(nums)
    for num in nums:
        rbt.insert(num)

    # search
    search_num = 23
    n = rbt.search(search_num)
    if n is not None:
        print(n)
    else:
        print('node {} not found'.format(search_num))

    # delete
    rbt.delete(4)

    # draw image
    # rbt.draw_img('rbt.png')
