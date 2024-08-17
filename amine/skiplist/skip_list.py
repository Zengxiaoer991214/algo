"""
@File    :   skip_list.py
@Time    :   2024/8/17 10:49
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
from typing import Optional, List
import random


class ListNode:
    def __init__(self, data: Optional[int] = None):
        self._data = data
        self._forwards: List[None | ListNode] = []

    @property
    def forwards(self):
        return self._forwards

    @property
    def data(self):
        return self._data

    @forwards.setter
    def forwards(self, value):
        self._forwards = value


class SkipList:
    _MAX_LEVEL = 16

    def __init__(self):
        self._level_count = 1
        self._head: ListNode = ListNode()
        self._head._forwards = [None] * type(self)._MAX_LEVEL

    def find(self, value: int) -> Optional[int]:
        p = self._head
        for i in range(self._level_count - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].data < value:
                p = p.forwards[i]
        return p.forwards[0] if p.forwards[0] and p.forwards[0].data == value else None

    def insert(self, value: int):
        level = self._random_level()
        if self._level_count < level:
            self._level_count = level
        new_node = ListNode(value)
        new_node.forwards = [None] * level
        update = [self._head] * level

        p = self._head
        for i in range(level - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].data < value:
                p = p.forwards[i]
            update[i] = p
        for i in range(level):
            new_node.forwards[i] = update[i].forwards[i]
            update[i].forwards[i] = new_node

    def delete(self, value):
        update: Optional[ListNode] = [None] * self._level_count
        p = self._head
        for i in range(self._level_count - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].data < value
                p = p.forwards[i]
            update[i] = p
        if p.forwards[0] and p.forwards[0].data == value:
            for i in range(self._level_count - 1, -1, -1):
                if update[i].forwards[i] and update[i].forwards[i].data == value:
                    update[i].forwards[i] = update[i].forwards[i].forwards[i]

    def __repr__(self):
        value = []
        p = self._head
        while p.forwards[0]:
            value.append(str(p.forwards[0].data))
            p = p.forwards[0]
        return "->".join(value)

    def _random_level(self, p: float = 0.5) -> int:
        level = 1
        while random.random() < p and level < type(self)._MAX_LEVEL:
            level += 1
        return level
