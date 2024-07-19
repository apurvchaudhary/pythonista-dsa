class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, value):
        current = self.root
        for i in value:
            node = current.child.get(i)
            if node is None:
                node = TrieNode()
                current.child[i] = node
            current = node
        current.end = True

    def search_string(self, value):
        current = self.root
        for i in value:
            node = current.child.get(i)
            if node is None:
                return False
            current = node
        if current.end is True:
            return True
        return False

    def delete_string(self, root, word, index):
        char = word[index]
        current_node: TrieNode = root.child.get(char)
        if not current_node:
            return False

        # case 1
        if len(current_node.child) > 1:
            self.delete_string(current_node, word, index + 1)
            return False

        # case 2
        if index == len(word) - 1:
            if len(current_node.child) >= 1:
                current_node.end = False
                return False
            root.child.pop(char)
            return True

        # case 3
        if current_node.end:
            self.delete_string(current_node, word, index + 1)
            return False

        can_be_deleted = self.delete_string(current_node, word, index + 1)
        if can_be_deleted:
            root.child.pop(char)
            return True
        return False


t = Trie()
t.insert_string("APP")
t.insert_string("PURV")
print(t.search_string("APP"))
