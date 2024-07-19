"""
Linked list programmings
"""


class Node:
    """
    single linked list node
    value - data of node
    next - pointer to next node
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Single Linked list with append method which add node at (end, start, middle)
    We have implemented traversing in __str__ method
    append() - add node at end O(1)
    prepend() - add node to start O(1)
    insert(index: int) - add node to specific index O(n)
    search(value) - to search for specific element O(n)
    get(index: int) - it will return the element stored on given index in single linked list
    set(index: int, value to update) - this will update value on given index
    pop_first() - return first element of linked list i.e. head element
    remove(index: int) - remove specific element via index
    delete_all() - delete all nodes
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    def remove(self, index):
        if index < 0 or index >= self.length:
            return "index error"
        if index == 0:
            self.pop_first()
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            if current.next is self.tail:
                current.next = None
                self.tail = current
            else:
                next_node = current.next.next
                current.next = next_node
        self.length -= 1

    def pop_first(self):
        head = self.head
        self.head = self.head.next
        if self.length == 1:
            self.tail = None
        self.length -= 1
        return head.value

    def set(self, index, value):
        node = self.get(index, return_type=1)
        node.value = value

    def get(self, index, return_type=0):
        current = self.head
        for _ in range(index):
            current = current.next
        if return_type == 0:
            return current.value
        return current

    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return True, index
            current = current.next
            index += 1
        return False

    def insert(self, index, value):
        if index > self.length or index < 0:
            raise IndexError(f"invalid index : index out of range")
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            node.next = temp_node.next
            temp_node.next = node
        self.length += 1

    def prepend(self, value):
        """
        adding node at start
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            head_node = self.head
            node.next = head_node
            self.head = node
        self.length += 1

    def append(self, value):
        """
        adding node by value at end
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            last_node = self.tail
            last_node.next = node
            self.tail = node
        self.length += 1

    def append_node(self, node: Node):
        """
        adding node at end
        :param node: Node
        :return: None
        """
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def reverse(self):
        prev_node = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head, self.tail = self.tail, self.head

    def delete_duplicates(self, head):
        current = head
        next_node = head.next
        while next_node is not None:
            if next_node.value == current.value:
                current.next = next_node.next
            else:
                current = next_node
            next_node = next_node.next
        return head

    def remove_elements(self, head, val):
        current = head
        prev = current
        while current is not None:
            if current.value == val:
                next_node = current.next
                if current is head:
                    head = next_node
                    prev = head
                else:
                    prev.next = next_node
            else:
                prev = current
            current = current.next

    def make_circular(self):
        self.tail.next = self.head

    def remove_duplicates(self):
        unique = {self.head.value}
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.value in unique:
                prev.next = current.next
            else:
                unique.add(current.value)
                prev = prev.next
            current = current.next

    def __str__(self):
        """
        string repr of class
        """
        temp = self.head
        result = "H---"
        while temp is not None:
            result += f"{temp.value}"
            if temp.next is not None:
                if temp is self.tail:
                    result += "---T"
                    break
                else:
                    result += "->"
            else:
                result += "---T"
            temp = temp.next
        return result
