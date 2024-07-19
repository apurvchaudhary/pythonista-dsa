"""
LRU cache is least recently used cache
for implementing this we will be using 2 Data Structures 1. Doubly linked list 2. Hash map
1. Doubly linked list - for maintaining order in o(1) time and space
2. Hashmap for storing key-value pair which has get and set with o(1) time and space in Average case
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            head_node = self.head
            node.next = head_node
            head_node.prev = node
            self.head = node
        self.length += 1

    def remove_from_end(self):
        tail_node = self.tail
        prev_node = tail_node.prev
        prev_node.next = None
        self.tail = prev_node
        self.length -= 1
        return tail_node.key

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        if node is self.tail:
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next = next_node
            next_node.prev = prev_node
        self.length -= 1

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result += f"{current.value}"
            if current.next is not None:
                result += "<->"
            current = current.next
        return result


class LruCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.list = DoublyLinkedList()

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.list.remove(node)
            self.list.add_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                _key = self.list.remove_from_end()
                del self.cache[_key]
            node = Node(key, value)
            self.cache[key] = node
            self.list.add_to_head(node)

    def get(self, key):
        if key not in self.cache:
            return "KeyError"
        node = self.cache[key]
        self.list.remove(node)
        self.list.add_to_head(node)
        return node.value


lru = LruCache(3)
lru.put(10, 10)
lru.put(20, 20)
lru.put(30, 30)
lru.put(10, 11)
lru.put(40, 40)
print(lru.get(20))
