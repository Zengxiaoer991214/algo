"""
@File    :   practice.py
@Time    :   2024/8/10 13:35
@Author  :   LinLi6
@Desc    :

@usage   :

"""
import sys
from typing import Optional

# 引用当前文件夹下的single_linked_list
sys.path.append('singly_linked_list')
from single_linked_list import SingleLinkedList, Node


def reverse(head: Node):
    """
    Reverse linked list
    :param head:
    :return:
    """
    reverse_head = None
    while head:
        next = head.next_node
        head.next_node = reverse_head
        reverse_head = head
        head = next

    return reverse_head


def is_palindrome(link: SingleLinkedList) -> bool:
    """
        Check if linked list element is a palindrome
    :param link:
    :return:
    """
    link.print_all()
    slow = link.head
    fast = link.head
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
    reversed = reverse(slow)
    head_node = link.head
    is_palin = True
    while head_node and reversed:
        if head_node.data == reversed.data:
            head_node = head_node.next_node
            reversed = reversed.next_node
        else:
            is_palin = False
            break

    return is_palin


def reverse_2(head: Node) -> Node:
    reversed_head: Optional[Node] = None
    cur = head
    while cur:
        reversed_head, reversed_head.next_node, cur = cur, reversed_head, reversed_head.next_node
    return reversed_head


def has_cycle(head: Node) -> bool:
    """
    check if the Linked List has Cycle
    :param head:
    :return:
    """
    slow, fast = head, head
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow == fast:
            return True
    return False


def merge_sorted_list(l1: Node, l2: Node) -> Optional[Node]:
    """
    Merge ordered linked lists
    :param l1:
    :param l2:
    :return:
    """
    if l1 and l2:
        p1, p2 = l1, l2
        fake_head = Node(None)
        cur = fake_head
        while p1 and p2:
            if p1.data <= p2.data:
                cur.next_node = p1
                p1 = p1.next_node
            else:
                cur.next_node = p2
                p2 = p2.next_node
            cur = cur.next_node
        cur.next_node = p1 if p1 else p2
        return fake_head.next_node
    return l1 or l2


def del_nth_from_end(head: Node, n: int) -> Optional[Node]:
    """
    Delete the last N nodes
    :param head:
    :param n:
    :return:
    """
    fast = head
    count = 0
    while fast and count < n:
        fast = fast.next_node
        count += 1
    if not fast and count < n:
        return head
    if not fast and count == n:
        return head.next_node


def del_nth_from_end_recursion(head: Node, n: int) -> Optional[Node]:
    """
    Delete the last N nodes
    :param head:
    :param n:
    :return:
    """

    def remove_helper(node: Node) -> int:
        if not node:
            return 0

        # 递归到链表末尾
        index = remove_helper(node._next) + 1

        # 当我们到达倒数第 n 个节点时，进行删除
        if index == n + 1:
            if node._next:
                node._next = node._next._next
            else:
                node._next = None

        return index

    dummy = Node(0)
    dummy._next = head
    remove_helper(dummy)
    return dummy


def find_middle_node(head: Node) -> Optional[Node]:
    """
    find the middle node
    :param head:
    :return:
    """
    slow, fast = head, head
    fast = fast.next_node if fast else None
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
    return slow


def print_all(head: Node):
    nums = []
    cur = head
    while cur:
        nums.append(cur.data)
        cur = cur.next_node
    print("->".join(str(num) for num in nums))


def reorder_list(head: Optional[Node]) -> None:
    """
    https://leetcode.cn/problems/reorder-list/
    :param head:
    :return:
    """
    if not head:
        return
    vec = list()
    node = head
    while node:
        vec.append(node)
        node = node.next_node
    i, j = 0, len(vec) - 1
    while i < j:
        vec[i].next_node = vec[j]
        i += 1
        if i == j:
            break
        vec[j].next_node = vec[i]
        j -= 1
    vec[i].next_node = None


if __name__ == '__main__':
    test_str_arr = ['ab', 'aa', 'aba', 'abba', 'abcba']
    for string in test_str_arr:
        link = SingleLinkedList()
        for i in string:
            link.insert_to_head(i)

        print(is_palindrome(link))
