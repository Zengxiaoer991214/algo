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
