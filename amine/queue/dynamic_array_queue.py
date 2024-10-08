"""
@File    :   dynamic_array_queue.py
@Time    :   2024/8/15 9:25
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
from typing import Optional


class DynamicArrayQueue:

    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def en_queue(self, item: str) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                return False

            self._items[0: self._tail - self._head] = self._items[self._head: self._tail]
            self._tail -= self._head
            self._head = 0
        if self._tail == len(self._items):
            self._items.append(item)
        else:
            self._items[self._tail] = item
        self._tail += 1
        return True

    def de_queue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item

    def __repr__(self) -> str:
        return " ".join(item for item in self._items[self._head: self._tail])


if __name__ == "__main__":
    q = DynamicArrayQueue(10)
    for i in range(10):
        q.en_queue(str(i))
    print(q)

    for _ in range(3):
        q.de_queue()
    print(q)

    q.en_queue("7")
    q.en_queue("8")
    print(q)
