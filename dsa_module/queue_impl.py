from stack_impl import Node, LinkedListStack


class Queue:
    def __init__(self):
        self.queue = []

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        if not self.queue:
            return True
        return False

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("queue is empty")
        return self.queue.pop(0)

    def __str__(self):
        return f"peek <- {self.queue} <- in"


class LinkedListQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.head = None
        self.tail = None
        self.length = 0

    def is_full(self):
        if self.length == self.max_size:
            return True
        return False

    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def enqueue(self, value):
        if self.is_full():
            raise ValueError("queue is full")
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def peek(self):
        if self.is_empty():
            raise ValueError("queue is empty")
        return self.head.value

    def dequeue(self):
        if self.is_empty():
            raise ValueError("queue is empty")
        if self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
        else:
            node = self.head
            self.head = self.head.next
            node.next = Node
        self.length -= 1
        return node.value

    def __str__(self):
        res = "out <- "
        current = self.head
        while current is not None:
            res += str(current.value)
            if current.next is not None:
                res += "<->"
            current = current.next
        res += " <- in"
        return res

    def delete(self):
        self.head = None
        self.head = None
        self.length = 0


if __name__ == "__main__":
    q = LinkedListQueue(3)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q)
