"""
@File    :   circular_queue.py
@Time    :   2024/8/15 8:38
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
from typing import Optional
from itertools import chain


class CircularQueue:

    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity + 1
        self._head = 0
        self._tail = 0

    def en_queue(self, item: str) -> bool:
        if (self._tail + 1) % self._capacity == self._head:
            return False
        self._items.append(item)
        self._tail = (self._tail + 1) % self._capacity
        return True

    def de_queue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head = (self._head + 1) % self._capacity
            return item

    def __repr__(self) -> str:
        if self._tail >= self._head:
            return " ".join(item for item in self._items[self._head: self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))


if __name__ == "__main__":
    q = CircularQueue(5)
    for i in range(5):
        q.en_queue(str(i))
    q.de_queue()
    q.de_queue()
    q.de_queue()
    q.de_queue()
    q.de_queue()
    q.de_queue()
    q.en_queue(str(5))
    print(q)
