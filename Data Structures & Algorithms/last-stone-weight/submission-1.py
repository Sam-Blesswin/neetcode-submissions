class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for n in stones:
            heapq.heappush(maxheap,-n)
        
        while len(maxheap)>1:
            y = heapq.heappop(maxheap)
            x = heapq.heappop(maxheap)
            
            heapq.heappush(maxheap, y-x)
        
        return -heapq.heappop(maxheap)

        