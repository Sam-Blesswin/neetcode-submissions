"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = defaultdict(Node)  
        hashmap[None] = None      
        
        cur = head
        while cur:
            if cur not in hashmap:
                hashmap[cur] = Node(cur.val)
            if cur.next not in hashmap:
                hashmap[cur.next] = Node(cur.next.val)
            if cur.random not in hashmap:
                hashmap[cur.random] = Node(cur.random.val)

            hashmap[cur].next = hashmap[cur.next]
            hashmap[cur].random = hashmap[cur.random]
            cur = cur.next

        return hashmap[head]

        

        