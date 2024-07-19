class Stack:
    """
    stack using python list
    """

    def __init__(self, size):
        self.stack = []
        self.size = size

    def is_empty(self):
        if not self.stack:
            return True
        return False

    def is_full(self):
        if len(self.stack) == self.size:
            return True
        return False

    def push(self, value):
        if self.is_full():
            raise ValueError("Stack is full")
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise ValueError("stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("stack is empty")
        return self.stack[len(self.stack) - 1]

    def delete(self):
        self.stack = None

    def __str__(self):
        return f"bottom - {self.stack} - Top"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack:
    """
    Stack using single linked list
    """

    def __init__(self, size):
        self.size = size
        self.head = None
        self.length = 0

    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def is_full(self):
        if self.length == self.size:
            return True
        return False

    def push(self, value):
        if self.is_full():
            raise ValueError("stack is full")
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("stack is empty")
        if self.head is self.tail:
            node = self.head
            self.head = None
        else:
            node = self.head
            self.head = self.head.next
            node.next = None
        self.length -= 1
        return node.value

    def peek(self):
        if self.is_empty():
            raise ValueError("stack is empty")
        return self.head.value

    def delete(self):
        self.head = None
        self.length = 0

    def __str__(self):
        result = "top - "
        current = self.head
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += "<->"
            current = current.next
        result += " - bottom"
        return result


class MinMaxStack:
    def __init__(self, size):
        self.stack = None
        self.min_node = None
        self.max_node = None
        self.size = size
        self.length = 0

    def get_min(self):
        if self.min_node:
            return self.min_node.value
        return None

    def get_max(self):
        if self.max_node:
            return self.max_node.value
        return None

    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def is_full(self):
        if self.length == self.size:
            return True
        return False

    def push(self, value):
        if self.is_full():
            raise ValueError("stack is full")
        if self.stack is None:
            self.min_node = Node(value)
            self.max_node = Node(value)
            self.stack = Node(value)
        else:
            if value <= self.min_node.value:
                node = Node(value)
                node.next = self.min_node
                self.min_node = node
            if value >= self.max_node.value:
                node = Node(value)
                node.next = self.max_node
                self.max_node = node
            node = Node(value)
            node.next = self.stack
            self.stack = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("stack is empty")
        node = self.stack
        if node.value == self.min_node.value:
            self.min_node = self.min_node.next
        if node.value == self.max_node.value:
            self.max_node = self.max_node.next
        self.stack = node.next
        node.next = None
        self.length -= 1
        return node.value

    def __str__(self):
        res = "Top -> "
        current = self.stack
        while current is not None:
            res += str(current.value)
            if current.next is not None:
                res += "->"
            current = current.next
        res += " <- bottom"
        return res


class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        if not self.stack:
            return True
        return False

    def peek(self):
        if self.is_empty():
            raise ValueError("stack is empty")
        return self.stack[-1][-1]

    def push(self, item):
        if len(self.stack) > 0 and len(self.stack[-1]) < self.capacity:
            self.stack[-1].append(item)
        else:
            self.stack.append([item])

    def pop(self):
        if self.is_empty():
            raise ValueError("stack is empty")
        item = self.stack[-1].pop()
        if not self.stack[-1]:
            del self.stack[-1]
        return item

    def pop_at(self, index):
        if not self.stack[index]:
            raise ValueError("stack is empty")
        return self.stack[index].pop()


class QueueUsingStack:
    def __init__(self, size):
        self.stack1 = Stack(size)
        self.stack2 = Stack(size)

    def enqueue(self, item):
        if self.stack1.is_full() and self.stack2.is_full():
            raise ValueError("both stack is full")
        elif self.stack1.is_full():
            while self.stack1.stack:
                item = self.stack1.pop()
                self.stack2.push(item)
        self.stack1.push(item)

    def dequeue(self):
        if not self.stack2.stack:
            while self.stack1.stack:
                item = self.stack1.pop()
                self.stack2.push(item)
        return self.stack2.pop()


q = QueueUsingStack(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
print("")
