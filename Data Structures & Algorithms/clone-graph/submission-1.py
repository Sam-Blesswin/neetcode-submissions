"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
            
        hashmap = {}
        def copy(node: Optional['Node']):
            if not node:
                return
            if node in hashmap:
                return
            hashmap[node] = Node(node.val)

            for n in node.neighbors:
                copy(n)
                hashmap[node].neighbors.append(hashmap[n])

        copy(node)
        return hashmap[node] 
        