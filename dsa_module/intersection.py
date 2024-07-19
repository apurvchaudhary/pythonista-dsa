import sys


inputs = []
for line in sys.stdin:
    if not line.strip():
        break
    inputs.append(line.strip())


class Node:
    """
    class to represent node which has two attribute
    1. value: value it holds
    2. next: next is ref to next node if not then None
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        self.nodes_dict = {}
        self.output = ()


def do_linked_lists_intersect(input_list: str, hashmap: HashMap):
    # for each input list in whole input list i.e a->b from ["a->b", "r->s"...]
    if "->" in input_list:
        l_and_r_node = input_list.split("->")
        # fetching left & right node key
        lnode, rnode = l_and_r_node[0], l_and_r_node[1]

        # if node key not in hashmap then create node & add to hashmap
        if lnode not in hashmap.nodes_dict:
            hashmap.nodes_dict[lnode] = Node(lnode)
        if rnode not in hashmap.nodes_dict:
            hashmap.nodes_dict[rnode] = Node(rnode)

        # add ref of nodes from left to right
        hashmap.nodes_dict[lnode].next = hash_map.nodes_dict[rnode]

    else:
        # set for keeping visited node check in o(1) time for intersection
        visited_nodes = set()

        for head in input_list.split(","):
            # set for keeping visited node check in o(1) time for acyclic purpose
            acyclic_check = set()
            # starting from current & traverse SLL
            current = hash_map.nodes_dict[head]

            while current is not None:
                # break inner & loop in both scenario either cyclic or intersection
                if current.value in acyclic_check:
                    # SLL is cyclic
                    return "Error Thrown!"
                if current.value in visited_nodes:
                    return True

                # add to both checks & move to next node
                visited_nodes.add(current.value)
                acyclic_check.add(current.value)
                current = current.next

        return False


hash_map = HashMap()

for inp in inputs:
    out = do_linked_lists_intersect(inp, hash_map)
    if out is not None:
        hash_map.output += (out,)

for out in hash_map.output:
    print(out)
