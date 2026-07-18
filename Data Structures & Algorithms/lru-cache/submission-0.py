class Node:
    def __init__(self, key, value):
        self.key = key 
        self.val = value
        self.prev, self.nex = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {} # key -> Node
        self.l = Node(None, None)
        self.r = Node(None, None)
        self.l.nex, self.r.prev = self.r, self.l 

    def insert(self, key, value):
        if key not in self.dic:
            self.dic[key] = Node(key, value)
        else:
            self.dic[key].val = value
        node = self.dic[key]
        right = self.r.prev
        right.nex, self.r.prev = node, node
        node.nex, node.prev = self.r, right

    def remove(self, key):
        node = self.dic[key]
        prev, nex = node.prev, node.nex
        prev.nex, nex.prev = nex, prev

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(key)
        self.insert(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        # update
        if key in self.dic:
            self.dic[key].val = value 
            self.remove(key)
            self.insert(key, value)
        elif len(self.dic) == self.cap:
            evict_key = self.l.nex.key
            self.remove(evict_key)
            del self.dic[evict_key]
            self.insert(key, value)
        else:
            self.insert(key, value)



