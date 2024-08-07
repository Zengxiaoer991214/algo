from typing import Optional


class Node:

    # def __init__(self, data: object, next_node: Optional['Node'] = None):
    def __init__(self, data: object, next_node=None):
        self.__data = data
        self.__next = next_node

    @property
    def data(self) -> object:
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        self.__next = next_node


class SingleLinkedList(object):
    def __init__(self):
        self.__head = None

    def find_by_value(self, value):
        node = self.__head
        while (node is not None) and (node.data != value):
            node = node.next_node
        return node

    def find_by_index(self, value) -> int:
        node = self.__head
        pos = 0
        while (node is not None) and (node.data != value):
            node = node.next_node
            pos = pos + 1
        return pos

    def insert_to_head(self, value):
        node = Node(value)
        node.next_node = self.__head
        self.__head = node

    def insert_after(self, node: Node, value):
        # if node is None:
        #     return
        new_node = Node(value)
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_before(self, node: Node, value):
        # if (node is None) or (self.__head is None):
        #     return
        if node == self.__head:
            self.insert_to_head(value)
            return

        new_node = Node(value)
        pro = self.__head
        not_found = False
        while pro.next_node != node:
            if pro.next_node is None:
                not_found = True
                break
            else:
                pro = pro.next_node

        if not not_found:
            pro.next_node = new_node
            new_node.next_node = node

    def delete_by_node(self, node: Node):

        if self.__head is None:
            return

        if node == self.__head:
            self.__head = node.next_node
            return

        pro = self.__head
        not_found = False
        while pro.next_node != node:
            if pro.next_node is None:
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            pro.next_node = node.next_node

    def delete_by_value(self, value):
        if self.__head is None:
            return

        if self.__head.data == value:
            self.__head = self.__head.next_node

        pro = self.__head
        node = pro.next_node
        not_found = False
        while node.data != value:
            if node.next_node is None:
                not_found = True
                break
            else:
                pro = node
                node = node.next_node
        if not not_found:
            pro.next_node = node.next_node

    def delete_last_n_node_two_point(self, n: int):
        fast = self.__head
        slow = self.__head
        step = 0
        tmp = None
        while step <= n:
            fast = fast.next_node
            step += 1
        while fast.next_node is not None:
            tmp = slow
            fast = fast.next_node
            slow = slow.next_node
        tmp.next_node = slow.next_node

    def delete_last_n_node(self, n: int):
        self.__delete_last_n_node(self.__head, n)

    def __delete_last_n_node(self, node: Node, n: int):
        if not self.__head:
            return 0
        index = self.__delete_last_n_node(node.next_node, n) + 1
        if index == n + 1:
            node.next_node = node.next_node.next_node
        return index

    def find_mid_node(self):
        pass


if __name__ == "__main__":
    linked_list = SingleLinkedList()
