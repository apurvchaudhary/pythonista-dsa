class Tree:
    """
    simple tree repr with using python list
    """

    def __init__(self, data):
        self.data = data
        self.child = []

    def add_child(self, tree_node):
        self.child.append(tree_node)

    def __str__(self, level=0):
        ret = " " * level + self.data + "\n"
        for ch in self.child:
            ret += ch.__str__(level + 1)
        return ret


drinks = Tree("drinks")
hot = Tree("hot")
cold = Tree("cold")
tea = Tree("tea")
coffee = Tree("coffee")
non_alc = Tree("non-alcoholic")
alc = Tree("alcoholic")
drinks.add_child(hot)
drinks.add_child(cold)
hot.add_child(tea)
hot.add_child(coffee)
cold.add_child(non_alc)
cold.add_child(alc)
print(drinks)
