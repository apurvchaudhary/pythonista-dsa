import crcmod
from sortedcontainers import SortedDict


crc16_func = crcmod.predefined.mkCrcFun('crc-16')


def get_hash_slot(key):
    crc = crc16_func(key.encode('utf-8'))
    return crc % 16384


class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.data = {}

    def __repr__(self):
        return f"Node({self.identifier})"


class RedisCluster:
    def __init__(self):
        self.nodes = SortedDict()
        self.hash_map = {}

    def add_node(self, identifier):
        new_node = Node(identifier)
        self._distribute_slots(new_node)
        self.hash_map[identifier] = new_node

    def remove_node(self, identifier):
        if identifier in self.hash_map:
            node = self.hash_map[identifier]
            self._reassign_slots(node)
            del self.hash_map[identifier]

    def _distribute_slots(self, new_node):
        # Distribute hash slots to the new node
        if not self.nodes:
            self.nodes[0] = new_node
        else:
            for slot in range(16384):
                if slot not in self.nodes:
                    self.nodes[slot] = new_node

    def _reassign_slots(self, node):
        # Reassign hash slots from the removed node to remaining nodes
        slots_to_reassign = [slot for slot, n in self.nodes.items() if n == node]
        for slot in slots_to_reassign:
            del self.nodes[slot]
        # Redistribute slots among remaining nodes
        for slot in slots_to_reassign:
            for remaining_node in self.hash_map.values():
                if slot not in self.nodes:
                    self.nodes[slot] = remaining_node
                    break

    def set(self, key, value):
        slot = get_hash_slot(key)
        node = self.nodes.peekitem(self.nodes.bisect_left(slot) % len(self.nodes))[1]
        node.data[key] = value

    def get(self, key):
        slot = get_hash_slot(key)
        node = self.nodes.peekitem(self.nodes.bisect_left(slot) % len(self.nodes))[1]
        return node.data.get(key, None)

    def __repr__(self):
        return f"RedisCluster(nodes={list(self.hash_map.keys())})"


cluster = RedisCluster()
cluster.add_node('nodeA')
cluster.add_node('nodeB')
cluster.add_node('nodeC')

cluster.set('mykey', 'myvalue')
print(cluster.get('mykey'))

print(cluster)

cluster.remove_node('nodeB')
print(cluster.get('mykey'))
print(cluster)
