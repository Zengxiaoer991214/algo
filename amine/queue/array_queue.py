"""
@File    :   queue.array_queue.py
@Time    :   2024/8/14 17:36
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
from typing import Optional


class ArrayQueue:
    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def en_queue(self, item: str) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                for i in range(self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0
        self._items.insert(self._tail, item)
        self._tail += 1
        return True

    def de_queue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        return None

    def __repr__(self) -> str:
        return " ".join(item for item in self._items[self._head: self._tail])
