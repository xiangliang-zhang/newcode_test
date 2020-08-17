class doubleLinkedNode:
    def __init__(self, val=None):
        self.val = val
        self.last = None
        self.next = None


class LRU:
    def __init__(self, k):
        self.k = k
        self.headnode = doubleLinkedNode()
        self.endnode = doubleLinkedNode()
        self.headnode.next = self.endnode
        self.endnode.last = self.headnode
        self.hashmap = {}

    def set(self, key, value):
        new_node = doubleLinkedNode((key, value))
        if self.headnode.next == self.endnode:
            self.headnode.next = new_node
            self.endnode.last = new_node
            new_node.last = self.headnode
            new_node.next = self.endnode
            self.hashmap[key] = new_node
            if len(self.hashmap) > self.k:
                self.removehead()
        elif key in self.hashmap:
            get_node = self.hashmap[key]
            get_node.val = (key, value)
            get_node.last.next = get_node.next
            get_node.next.last = get_node.last
            get_node.next = self.endnode
            get_node.last = self.endnode.last
            self.endnode.last.next = get_node
            self.endnode.last = get_node
        else:
            self.endnode.last.next = new_node
            new_node.last = self.endnode.last
            self.endnode.last = new_node
            new_node.next = self.endnode
            self.hashmap[key] = new_node
            if len(self.hashmap) > self.k:
                self.removehead()

    def removehead(self):
        result = self.headnode.next.val[0]
        self.headnode.next.next.last = self.headnode
        self.headnode.next.last = None
        self.headnode.next.next = None
        self.headnode.next = self.headnode.next.next
        del self.hashmap[result]

    def get(self, key):
        if not key or key not in self.hashmap:
            return None
        else:
            value = self.hashmap[key].val[1]
            self.set(key, value)
        return value


cache = LRU(3)
cache.set('A', 1)
cache.set('B', 2)
cache.set('C', 3)
cache.set('D', 4)
print(cache.get('A'))
print(cache.get('B'))
cache.set('A', 1)
print(cache.get('C'))
print(cache.get('D'))
cache.set('B', 1)
print(cache.get('B'))
