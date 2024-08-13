arr = [7, 10, 4, 3, 20, 15, 0, 23]


class MinHeap:

    heap = []

    @staticmethod
    def parent_index(index):
        return (index - 1) // 2

    def push(self, value):
        if not self.heap:
            self.heap.append(value)
        else:
            self.heap.append(value)
            self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise ValueError("heap is empty")
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(0)
        return value

    def heapify_up(self, index):
        while index > 0:
            parent = self.parent_index(index)
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        while 2 * index + 1 < len(self.heap):
            child = 2 * index + 1
            if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                child += 1
            if self.heap[child] < self.heap[index]:
                self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
                index = child
            else:
                break


m = MinHeap()
for i in arr:
    m.push(i)

for _ in range(len(arr)):
    arr[_] = m.pop()

print(arr)
