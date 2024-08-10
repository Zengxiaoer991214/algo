import operator
from typing import Optional

"""
@File    :   lru_cache.py
@Time    :   2024/8/10 11:19
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""


class DbListNode(object):
    def __init__(self, x: int, y: int):
        self.key: int = x
        self.val: int = y
        self.next: Optional[DbListNode] = None
        self.prev: Optional[DbListNode] = None


class LruCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hkeys: [int, int] = {}
        self.top = DbListNode(None, -1)
        self.tail = DbListNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, key: int) -> int:
        if key in self.hkeys.keys():
            cur: DbListNode = self.hkeys[key]
            cur.next.prev = cur.prev
            cur.prev.next = cur.next

            self.__put_on_head(cur)
            return self.hkeys[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.val = value
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            self.__put_on_head(cur)

        else:
            cur = DbListNode(key, value)
            self.hkeys[key] = cur

            self.__put_on_head(cur)
            if len(self.hkeys.keys()) > self.cap:
                self.hkeys.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)

    def __put_on_head(self, cur):
        top_node = self.top.next
        self.top.next = cur
        cur.prev = self.top
        cur.next = top_node
        top_node.prev = cur


if __name__ == '__main__':
    cache = LruCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)  # 返回  1
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    print(cache)
    cache.get(2)  # 返回 -1 (未找到)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    print(cache)
    cache.get(1)  # 返回 -1 (未找到)
    cache.get(3)  # 返回  3
    print(cache)
    cache.get(4)  # 返回  4
    print(cache)
