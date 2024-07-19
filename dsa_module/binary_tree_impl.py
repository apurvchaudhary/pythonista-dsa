from queue_impl import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


n1 = TreeNode("n1")
n2 = TreeNode("n2")
n3 = TreeNode("n3")
n4 = TreeNode("n4")
n5 = TreeNode("n5")
n6 = TreeNode("n6")
n7 = TreeNode("n7")
n8 = TreeNode("n8")
n9 = TreeNode("n9")
n10 = TreeNode("n10")
n11 = TreeNode("n11")
n1.left_child, n1.right_child = n2, n3
n2.left_child, n2.right_child = n4, n5
n3.left_child, n3.right_child = n6, n7
n4.left_child, n4.right_child = n8, n9
n5.left_child = n10


def preorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    print(root_node.data)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)


def inorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    inorder_traversal(root_node.left_child)
    print(root_node.data)
    inorder_traversal(root_node.right_child)


def postorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    postorder_traversal(root_node.left_child)
    postorder_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node: TreeNode):
    if not root_node:
        return
    q = Queue()
    q.enqueue(root_node)
    while not q.is_empty():
        node = q.dequeue()
        print(node.data)
        if node.left_child is not None:
            q.enqueue(node.left_child)
        if node.right_child is not None:
            q.enqueue(node.right_child)


# search node in Btree (using level order traversal)
def search_node_by_level_order_traversal(root_node: TreeNode, value: str):
    if not root_node:
        return
    if root_node.data == value:
        return True
    q = Queue()
    q.enqueue(root_node)
    while not q.is_empty():
        dequeued_node = q.dequeue()
        if (
            value == dequeued_node.data
            or value == dequeued_node.left_child.data
            or value == dequeued_node.right_child.data
        ):
            return True
        if dequeued_node.left_child is not None:
            q.enqueue(dequeued_node.left_child)
        if dequeued_node.right_child is not None:
            q.enqueue(dequeued_node.right_child)
    return False


# insert a node in BTree (using level order traversal)
def insert_node_by_level_order_traversal(root_node: TreeNode, node: TreeNode):
    if not root_node:
        root_node = node
    else:
        q = Queue()
        q.enqueue(root_node)
        while not q.is_empty():
            dequeued_node = q.dequeue()
            if not dequeued_node.left_child:
                dequeued_node.left_child = node
                return True
            else:
                q.enqueue(dequeued_node.left_child)
            if not dequeued_node.right_child:
                dequeued_node.right_child = node
                return True
            else:
                q.enqueue(dequeued_node.right_child)
    return True


# delete a node from Btree (using level order traversal)
def get_deepest_node_in_level_order_traversal(root_node: TreeNode):
    if not root_node:
        return
    q = Queue()
    dequeued_node = root_node
    q.enqueue(root_node)
    while not q.is_empty():
        dequeued_node = q.dequeue()
        if dequeued_node.left_child:
            q.enqueue(dequeued_node.left_child)
        if dequeued_node.right_child:
            q.enqueue(dequeued_node.right_child)
    return dequeued_node


def update_node_in_level_order_traversal(root_node: TreeNode, deepest: TreeNode, node: TreeNode):
    if not root_node:
        return
    q = Queue()
    q.enqueue(root_node)
    while not q.is_empty():
        dequeued_node = q.dequeue()
        if dequeued_node == node:
            dequeued_node.data = deepest.data
        if dequeued_node.left_child:
            q.enqueue(dequeued_node.left_child)
        if dequeued_node.right_child:
            q.enqueue(dequeued_node.right_child)


def delete_deepest_node_level_order_traversal(root_node: TreeNode, deepest: TreeNode):
    if not root_node:
        return
    q = Queue()
    q.enqueue(root_node)
    while not q.is_empty():
        dequeued_node = q.dequeue()
        if dequeued_node.left_child:
            if dequeued_node.left_child is deepest:
                dequeued_node.left_child = None
                break
            q.enqueue(dequeued_node.left_child)
        if dequeued_node.right_child:
            if dequeued_node.right_child is deepest:
                dequeued_node.right_child = None
                break
            q.enqueue(dequeued_node.left_child)


def delete_node(root_node: TreeNode, node: TreeNode):
    deepest = get_deepest_node_in_level_order_traversal(root_node)
    update_node_in_level_order_traversal(root_node, deepest, node)
    delete_deepest_node_level_order_traversal(root_node, deepest)


# preorder_traversal(n1)
# inorder_traversal(n1)
# postorder_traversal(n1)
# level_order_traversal(n1)
# insert_node_by_level_order_traversal(n1, n11)
# print(search_node_by_level_order_traversal(n1, n11))
# delete_node(n1, n3)
# level_order_traversal(n1)


# binary tree using python list
class BinaryTree:
    def __init__(self, max_size):
        self.max_size = max_size
        self.memory = max_size * [None]
        self.last_index = 0

    def add_child(self, value):
        if self.last_index + 1 == self.max_size:
            raise ValueError("memory full")
        self.memory[self.last_index + 1] = value
        self.last_index += 1

    def search(self, value):
        for i in self.memory:
            if i == value:
                return "Yes"
        return "No"

    def pre_order_traversal(self, index):
        if index > self.last_index:
            return
        print(self.memory[index])
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal(index * 2 + 1)

    def in_order_traversal(self, index):
        if index > self.last_index:
            return
        self.in_order_traversal(2 * index)
        print(self.memory[index])
        self.in_order_traversal(2 * index + 1)

    def post_order_traversal(self, index):
        if index > self.last_index:
            return
        self.in_order_traversal(2 * index)
        self.in_order_traversal(2 * index + 1)
        print(self.memory[index])

    def level_order_traversal(self, index):
        for i in range(index, self.last_index + 1):
            print(self.memory[i])

    def delete_node(self, value):
        if self.last_index == 0:
            raise ValueError("No node")
        for i in range(1, self.last_index + 1):
            if self.memory[i] == value:
                self.memory[i] = self.memory[self.last_index]
                self.memory[self.last_index] = None
                self.last_index -= 1


bt = BinaryTree(5)
bt.add_child(1)
bt.add_child(2)
bt.add_child(3)
bt.add_child(4)
bt.delete_node(3)
print(bt.search(3))
bt.level_order_traversal(1)
