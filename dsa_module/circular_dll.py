class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            node.next = self.head
            self.tail = node

    def delete_dll(self):
        self.head.prev = None
        self.tail.next = None
        self.head = self.tail = None

    def __str__(self):
        result = "T-H<->"
        current = self.head
        while current is not None:
            result += str(current.value)
            if current is self.tail:
                break
            result += "<->"
            current = current.next
        result += "<->T-H"
        return result


cdll = CDLL()
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.append(40)
cdll.append(50)
cdll.delete_dll()
print(cdll)
