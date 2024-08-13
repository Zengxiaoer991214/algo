"""
@File    :   linked_stack.py
@Time    :   2024/8/12 15:02
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
from typing import Optional
from algo.amine.linkedlist.single_linked_list import Node


class LinkedStack:
    def __init__(self):
        self.__top: Optional[Node] = None

    @property
    def top(self) -> Node:
        return self.__top

    def push(self, value: int):
        new_top = Node(value)
        new_top.next_node = self.top
        self.__top = new_top

    def pop(self) -> Optional[int]:
        res = None
        if self.top:
            res = self.top.data
            self.__top = self.__top.next_node
        return res

    def __repr__(self):
        current = self.__top
        nums = []
        while current:
            nums.append(current.data)
            current = current.next_node
        return " ".join(f"[{num}]" for num in nums)


if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)