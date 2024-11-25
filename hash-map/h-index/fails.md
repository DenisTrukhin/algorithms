1. Изначально пошел не по правильному пути, накручивал и усложнял при последующих попытках, надо было сразу начинать заново и подумать над другим решением 


```python
import hashlib

def hash_function(key):
    return int(hashlib.md5(key.encode()).hexdigest(), 16)

class ConsistentHash:
    def __init__(self, nodes, virtual_nodes=100):
        self.nodes = nodes
        self.virtual_nodes = virtual_nodes
        self.ring = {}
        self._build_ring()

    def _build_ring(self):
        for node in self.nodes:
            for i in range(self.virtual_nodes):
                key = self._hash(f"{node}:{i}")
                self.ring[key] = node

    def _hash(self, key):
        return hash_function(key)

    def get_node(self, key):
        if not self.ring:
            return None
        hash_key = self._hash(key)
        for node_hash in sorted(self.ring.keys()):
            if node_hash >= hash_key:
                return self.ring[node_hash]
        return self.ring[sorted(self.ring.keys())[0]]

    def add_node(self, node):
        for i in range(self.virtual_nodes):
            key = self._hash(f"{node}:{i}")
            self.ring[key] = node

    def remove_node(self, node):
        for i in range(self.virtual_nodes):
            key = self._hash(f"{node}:{i}")
            if key in self.ring:
                del self.ring[key]
```