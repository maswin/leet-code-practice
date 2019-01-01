# https://leetcode.com/problems/lru-cache/description/


class LRUCache:

    class Node:
        def __init__(self, key, value, next, prev):
            self.key = key
            self.val = value
            self.next = next
            self.prev = prev

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.count = 0
        self.capacity = capacity
        self.cache_head = self.Node(None, None, None, None)
        self.cache_tail = self.Node(None, None, None, None)
        self.cache_head.next = self.cache_tail
        self.cache_tail.prev = self.cache_head
        self.cache_index = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache_index:
            node = self.cache_index[key]
            self.update(node)
            return node.val
        return -1

    def add(self, node):
        self.count += 1
        self.cache_index[node.key] = node
        node.prev = self.cache_tail.prev
        self.cache_tail.prev.next = node
        node.next = self.cache_tail
        self.cache_tail.prev = node

    def remove(self, node):
        self.count -= 1
        if node.key in self.cache_index:
            del self.cache_index[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def update(self, node):
        self.remove(node)
        self.add(node)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache_index:
            node = self.cache_index[key]
            node.val = value
            self.update(node)
        else:
            node = self.Node(key, value, self.cache_tail.prev, self.cache_tail)
            self.add(node)
            if self.count > self.capacity:
                self.remove(self.cache_head.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
