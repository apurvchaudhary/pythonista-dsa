class MinHeap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def get_parent_index(index):
        return (index - 1) // 2

    def push(self, value):
        if not self.heap:
            self.heap.append(value)
        else:
            self.heap.append(value)
            self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return -1
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify_down(0)
            return root

    def heapify_up(self, index):
        while index > 0:
            parent_index = self.get_parent_index(index)
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        while 2 * index + 1 < len(self.heap):
            child_index = 2 * index + 1
            if child_index + 1 < len(self.heap) and self.heap[child_index + 1] < self.heap[child_index]:
                child_index += 1
            if self.heap[index] > self.heap[child_index]:
                self.heap[index], self.heap[child_index] = self.heap[child_index], self.heap[index]
                index = child_index
            else:
                break


h = MinHeap()
h.push(10)
h.push(5)
h.push(1)
h.push(6)
h.push(9)
h.push(15)
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())


class MaxHeap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def get_parent_index(index):
        return (index - 1) // 2

    def push(self, value):
        if not self.heap:
            self.heap.append(value)
        else:
            self.heap.append(value)
            self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return -1
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify_down(0)
            return root

    def heapify_up(self, index):
        while index > 0:
            parent_index = self.get_parent_index(index)
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        while 2 * index + 1 < len(self.heap):
            child_index = 2 * index + 1
            if child_index + 1 < len(self.heap) and self.heap[child_index + 1] > self.heap[child_index]:
                child_index += 1
            if self.heap[index] < self.heap[child_index]:
                self.heap[index], self.heap[child_index] = self.heap[child_index], self.heap[index]
                index = child_index
            else:
                break


h = MaxHeap()
h.push(10)
h.push(5)
h.push(1)
h.push(6)
h.push(9)
h.push(15)
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
