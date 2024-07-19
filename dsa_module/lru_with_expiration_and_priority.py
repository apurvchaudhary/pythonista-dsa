class MinHeap:
    def __init__(self, comparison_key):
        self.heap = []
        self.node_dict = {}
        self.comparison_key = comparison_key

    @staticmethod
    def get_parent_index(index):
        return (index - 1) // 2

    def push(self, node):
        self.node_dict[node] = len(self.heap)
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            node = self.heap.pop()
            del self.node_dict[node]
            return node
        min_node = self.heap[0]
        del self.node_dict[min_node]
        farthest_node = self.heap.pop()
        self.heap[0] = farthest_node
        self.node_dict[farthest_node] = 0
        self.heapify_down(0)
        return min_node

    def heapify_up(self, index):
        while index > 0:
            parent_index = self.get_parent_index(index)
            if self.get_comparison_value(self.heap[index]) < self.get_comparison_value(self.heap[parent_index]):
                self.swap_nodes(index, parent_index)
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        while 2 * index + 1 < len(self.heap):
            child_index = 2 * index + 1
            if child_index + 1 < len(self.heap) and self.get_comparison_value(
                self.heap[child_index + 1]
            ) < self.get_comparison_value(self.heap[child_index]):
                child_index += 1
            if self.get_comparison_value(self.heap[child_index]) < self.get_comparison_value(self.heap[index]):
                self.swap_nodes(index, child_index)
                index = child_index
            else:
                break

    def get_comparison_value(self, node):
        return getattr(node, self.comparison_key)

    def swap_nodes(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.node_dict[self.heap[i]], self.node_dict[self.heap[j]] = j, i


class ExpiryHeap(MinHeap):
    def __init__(self):
        super().__init__("expiry")


class PriorityHeap(MinHeap):
    def __init__(self):
        super().__init__("priority")


class Node:
    def __init__(self, key, value, priority, expiry):
        self.key = key
        self.value = value
        self.priority = priority
        self.expiry = expiry
        self.next = None
        self.prev = None


class Dll:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def remove_tail(self):
        if self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
        else:
            node = self.tail
            self.tail = self.tail.prev
            node.prev = None
        return node

    def remove_node(self, node):
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.priority_heap = PriorityHeap()
        self.expiry_heap = ExpiryHeap()
        self.priority_hashmap = dict()
        self.curr_time = 5000

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            dll: Dll = self.priority_hashmap[node.priority]
            if dll.head is not node:
                dll.remove_node(node)
                dll.add_to_head(node)
            return node.value
        else:
            return f"{key} not found"

    def set(self, key, value, expiry, priority):
        if key in self.cache:
            node: Node = self.cache[key]
            node.value = value
            if expiry != node.expiry:
                node_expiry_index = self.expiry_heap.node_dict[node]
                if expiry < node.expiry:
                    node.expiry = expiry
                    self.expiry_heap.heapify_up(node_expiry_index)
                else:
                    node.expiry = expiry
                    self.expiry_heap.heapify_down(node_expiry_index)
            if priority != node.priority:
                old_dll: Dll = self.priority_hashmap[node.priority]
                old_dll.remove_node(node)
                if priority in self.priority_hashmap:
                    dll: Dll = self.priority_hashmap[priority]
                    dll.add_to_head(node)
                else:
                    dll = Dll()
                    dll.add_to_head(node)
                    self.priority_hashmap[priority] = dll
                node_priority_index = self.priority_heap.node_dict[node]
                if priority < node.priority:
                    node.priority = priority
                    self.priority_heap.heapify_up(node_priority_index)
                else:
                    node.priority = priority
                    self.priority_heap.heapify_down(node_priority_index)
            else:
                dll: Dll = self.priority_hashmap[node.priority]
                if dll.head is not node:
                    dll.remove_node(node)
                    dll.add_to_head(node)

        else:
            if len(self.cache) == self.capacity:
                self.eviction()
            node = Node(key, value, priority, expiry)
            self.cache[key] = node
            self.priority_heap.push(node)
            self.expiry_heap.push(node)
            if priority in self.priority_hashmap:
                dll: Dll = self.priority_hashmap[priority]
            else:
                dll = Dll()
                self.priority_hashmap[node.priority] = dll
            dll.add_to_head(node)

    def eviction(self):
        if self.expiry_heap.heap[0].expiry < self.curr_time:
            expiry_node = self.expiry_heap.pop()
            priority_node_index = self.priority_heap.node_dict[expiry_node]
            farthest_priority_node = self.priority_heap.heap.pop()
            self.priority_heap.node_dict[farthest_priority_node] = priority_node_index
            self.priority_heap.heap[priority_node_index] = farthest_priority_node
            self.priority_heap.heapify_down(priority_node_index)
            dll: Dll = self.priority_hashmap[expiry_node.priority]
            dll.remove_node(expiry_node)
            del self.priority_heap.node_dict[expiry_node]
            del self.cache[expiry_node.key]
        else:
            min_priority_node = self.priority_heap.heap[0]
            dll: Dll = self.priority_hashmap[min_priority_node.priority]
            removed_node = dll.remove_tail()
            if removed_node is min_priority_node:
                self.priority_heap.pop()
            else:
                node_priority_index = self.priority_heap.node_dict[removed_node]
                farthest_priority_node = self.priority_heap.pop()
                self.priority_heap.heap[node_priority_index] = farthest_priority_node
                self.priority_heap.node_dict[farthest_priority_node] = node_priority_index
                self.priority_heap.heapify_down(node_priority_index)
                del self.priority_heap.node_dict[removed_node]
            node_expiry_index = self.expiry_heap.node_dict[removed_node]
            farthest_expiry_node = self.expiry_heap.heap.pop()
            self.expiry_heap.heap[node_expiry_index] = farthest_expiry_node
            self.expiry_heap.node_dict[farthest_expiry_node] = node_expiry_index
            self.expiry_heap.heapify_down(node_expiry_index)
            del self.expiry_heap.node_dict[removed_node]
            del self.cache[removed_node.key]


lru = LRU(5)
lru.set("A", 5, 10001, 5)
lru.set("B", 4, 40006, 1)
lru.set("C", 3, 10001, 5)
lru.set("D", 2, 500, 9)
lru.set("E", 1, 10004, 5)
print(lru.get("C"))
lru.curr_time = 900
lru.set("F", 10, 5001, 5)
print(lru.get("D"))
lru.set("G", 9, 5004, 5)
print(lru.get("B"))
lru.set("H", -1, 5009, 5)
print(lru.get("A"))
lru.set("I", 1, 50011, 5)
print(lru.get("E"))
lru.set("C", 1, 5021, 5)
print(lru.get("D"))
