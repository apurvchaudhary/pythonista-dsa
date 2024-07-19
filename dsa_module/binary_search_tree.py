from queue_impl import Queue


class BstNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def preorder_traversal(node: BstNode):
    if node is None:
        return
    print(node.value)
    preorder_traversal(node.left_child)
    preorder_traversal(node.right_child)


def in_order_traversal(node: BstNode):
    if node is None:
        return
    in_order_traversal(node.left_child)
    print(node.value)
    in_order_traversal(node.right_child)


def post_order_traversal(node: BstNode):
    if node is None:
        return
    post_order_traversal(node.left_child)
    post_order_traversal(node.right_child)
    print(node.value)


def level_order_traversal(node: BstNode):
    if node is None:
        return
    q = Queue()
    q.enqueue(node)
    while not q.is_empty():
        node = q.dequeue()
        print(node.value)
        if node.left_child:
            q.enqueue(node.left_child)
        if node.right_child:
            q.enqueue(node.right_child)


def insert_node(root_node: BstNode, value):
    if root_node.value is None:
        root_node.value = value
    elif value <= root_node.value:
        if root_node.left_child is None:
            root_node.left_child = BstNode(value)
        else:
            return insert_node(root_node.left_child, value)
    else:
        if root_node.right_child is None:
            root_node.right_child = BstNode(value)
        else:
            return insert_node(root_node.right_child, value)


def search_node(root_node: BstNode, value):
    if root_node is None:
        return False
    elif root_node.value == value:
        return True
    elif value <= root_node.value:
        return search_node(root_node.left_child, value)
    else:
        return search_node(root_node.right_child, value)


r = BstNode(70)
insert_node(r, 50)
insert_node(r, 30)
insert_node(r, 90)
insert_node(r, 60)
insert_node(r, 80)
insert_node(r, 100)
insert_node(r, 20)
insert_node(r, 40)
