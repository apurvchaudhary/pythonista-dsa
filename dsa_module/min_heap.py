class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MinHeap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def get_parent_index(index):
        return (index - 1) // 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def add_child(self, value):
        if not self.heap:
            self.heap.append(value)
        else:
            self.heap.append(value)
            self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.heap:
            root = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.heapify_down(0)
            print(root)
        return -1

    def heapify_up(self, index):
        while index > 0:
            if self.heap[index] < self.heap[self.get_parent_index(index)]:
                self.swap(index, self.get_parent_index(index))
                index = self.get_parent_index(index)
            else:
                break

    def heapify_down(self, index):
        while 2 * index + 1 < len(self.heap):
            child = 2 * index + 1
            if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                child += 1
            if self.heap[child] < self.heap[index]:
                self.swap(child, index)
                index = child
            else:
                break


m = MinHeap()
m.add_child(10)
m.add_child(8)
m.add_child(5)
m.add_child(2)
m.add_child(20)
m.add_child(1)
print(m.heap)
m.pop()
m.pop()
m.pop()
m.pop()
m.pop()
m.pop()
m.pop()
