class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"<- {self.value} ->"


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError(f"[{index}] Index out of range")
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            if index == 0:
                self.pop_first()
            elif index == self.length - 1:
                self.pop()
            else:
                current = self.get(index)
                prev_node = current.prev
                next_node = current.next
                prev_node.next = next_node
                next_node.prev = prev_node
                current.next = None
                current.prev = None
        self.length -= 1

    def pop(self):
        if self.length == 0:
            raise IndexError("[0] Index out of range")
        if self.length == 1:
            popped_node = self.tail
            self.head = None
            self.tail = None
            popped_node.prev = None
        else:
            popped_node = self.tail
            prev_node = self.tail.prev
            prev_node.next = None
            popped_node.prev = None
            self.tail = prev_node
        self.length -= 1
        return popped_node

    def pop_first(self):
        if self.length == 0:
            raise IndexError("[0] Index out of range")
        if self.length == 1:
            popped = self.head
            self.head = None
            self.tail = None
        else:
            popped = self.head
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
        self.length -= 1
        return popped.value

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError(f"[{index}] Index out of range")
        node = Node(value)
        if index == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            current = self.get(index - 1)
            next_node = current.next
            node.next = next_node
            next_node.prev = node
            current.next = node
            node.prev = current
        self.length += 1

    def set(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError(f"[{index}] Index out of range")
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError(f"[{index}] Index out of range")
        if index < self.length / 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - index - 1):
                current = current.prev
        return current

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return True, index
            current = current.next
            index += 1
        return False, None

    def reverse_traversal(self):
        current = self.tail
        result = "T<->"
        while current:
            result += str(current.value)
            if current.prev:
                result += "<->"
            current = current.prev
        result += "<->H"
        return result

    def prepend(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            prev_node = self.tail
            prev_node.next = node
            node.prev = prev_node
            self.tail = node
        self.length += 1

    def __str__(self):
        current = self.head
        result = "H<->"
        while current:
            result += str(current.value)
            if current.next:
                result += "<->"
            current = current.next
        result += "<->T"
        return result


dll = DLL()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
print(dll)
dll.remove(1)
print(dll)
