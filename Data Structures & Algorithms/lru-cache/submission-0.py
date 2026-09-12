class LRUCache:

    class Node:
        val: int
        prev: Node
        next: Node

        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    size: int
    least: Node
    most: Node
    memory: dict

    def __init__(self, capacity: int):
        self.size = capacity
        self.least = self.Node(-1,-1)
        self.most = self.Node(-1,-1)

        self.least.next = self.most
        self.most.prev = self.least

        self.memory = {}


    def get(self, key: int) -> int:
        if key not in self.memory:
            return -1
        
        node = self.memory[key]
        self.remove(node)
        self.add(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.memory:
            node = self.memory[key]
            node.val = value
            self.remove(node)
        else:
            node = self.Node(key, value)

        self.memory[key] = node

        if len(self.memory) > self.size:
            leastNode = self.least.next
            self.remove(leastNode)
            del self.memory[leastNode.key]
        
        self.add(node)

    def add(self, node: Optional[Node]):
        prev = self.most.prev
        prev.next = node
        node.next = self.most

        self.most.prev = node
        node.prev = prev

        
    def remove(self, node: Optional[Node]):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev
        
