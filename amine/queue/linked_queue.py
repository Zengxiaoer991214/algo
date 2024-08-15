"""
@File    :   linked_queue.py
@Time    :   2024/8/15 9:07
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
from typing import Optional


class Node:

    def __init__(self, data: str, next=None):
        self.data = data
        self._next: Optional[Node] = next

    @property
    def next(self):
        return self._next


class LinkedQueue:

    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None

    def en_queue(self, value: str):
        new_node = Node(value)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node

    def de_queue(self) -> Optional[str]:
        if self._head:
            value = self._head.data
            self._head = self._head.next
            if not self._head:
                self._tail = None
            return value

    def __repr__(self) -> str:
        values = []
        current = self._head
        while current:
            values.append(current.data)
            current = current._next
        return "->".join(value for value in values)


if __name__ == "__main__":
    q = LinkedQueue()
    for i in range(10):
        q.en_queue(str(i))
    print(q)

    for _ in range(3):
        q.de_queue()
    print(q)

    q.en_queue("7")
    q.en_queue("8")
    print(q)
