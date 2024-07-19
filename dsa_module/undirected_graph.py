class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent_nodes = {}
        self.visited = 0

    def __str__(self):
        return self.value


class Tree:
    def __init__(self):
        self.root = None
        self.nodes = {}

    def add_root(self, value):
        if not self.root:
            node = Node(value)
            self.root = node
            self.nodes[value] = node
        return

    def is_cyclic(self, queue=[]):
        if not queue:
            if self.root.visited != 0:
                return False
            self.root.visited = 1
            queue.append(self.root)
            return self.is_cyclic(queue)
        else:
            node = queue.pop()
            print(f"visited : {node.value}")
            for n in node.adjacent_nodes:
                n = self.nodes[n]
                if n.visited == 2:
                    continue
                elif n.visited == 1:
                    return True
                else:
                    n.visited = 1
                    queue.append(n)
            return self.is_cyclic(queue)

    def add_child(self, parent, child_value):
        parent = self.nodes[parent]
        if child_value not in self.nodes:
            node = Node(child_value)
            self.nodes[child_value] = node
        parent.adjacent_nodes[child_value] = self.nodes[child_value]


t = Tree()
t.add_root("A")
t.add_child("A", "B")
t.add_child("A", "C")
t.add_child("B", "D")
t.add_child("B", "E")
t.add_child("C", "E")
print(t.is_cyclic())
