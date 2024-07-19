class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, node, new_node):
        new_node.next = node.next
        new_node.prev = node
        node.next.prev = new_node
        node.next = new_node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.node_map = {}  # key -> Node
        self.freq_map = {}  # frequency -> DoublyLinkedList
        self.min_freq = 0

    def update_frequency(self, node):
        # Remove node from its current frequency list
        freq_list = self.freq_map[node.freq]
        freq_list.remove_node(node)

        # If the current frequency list is empty and it is the minimum frequency, update min_freq
        if self.min_freq == node.freq and not freq_list.head.next.next:
            self.min_freq += 1

        # Increase the frequency of the node and insert it into the new frequency list
        node.freq += 1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()
        new_freq_list = self.freq_map[node.freq]
        new_freq_list.insert_after(new_freq_list.head, node)

    def get(self, key):
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        self.update_frequency(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self.update_frequency(node)
        else:
            if len(self.node_map) == self.capacity:
                # Evict the least frequently used node
                min_freq_list = self.freq_map[self.min_freq]
                evicted_node = min_freq_list.tail.prev
                min_freq_list.remove_node(evicted_node)
                del self.node_map[evicted_node.key]

            # Add new node to the cache
            new_node = Node(key, value)
            self.node_map[key] = new_node
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            new_freq_list = self.freq_map[1]
            new_freq_list.insert_after(new_freq_list.head, new_node)
            self.min_freq = 1


# Example usage:
lfu_cache = LFUCache(2)
lfu_cache.put(1, 1)
lfu_cache.put(2, 2)
print(lfu_cache.get(1))
print(lfu_cache.get(2))  # Output: 1
lfu_cache.put(3, 3)  # Remove key 2
print(lfu_cache.get(2))  # Output: -1 (not found)
print(lfu_cache.get(3))  # Output: 3
