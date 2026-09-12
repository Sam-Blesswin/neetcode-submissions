class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = defaultdict(int)
        for task in tasks:
            hashmap[task] += 1
        
        maxheap = []
        for k,v in hashmap.items():
            heapq.heappush(maxheap,-v)

        counter = 0
        queue = deque()

        while maxheap or queue:
            if maxheap:
                val = -heapq.heappop(maxheap)
                val-=1
                if val:
                    queue.append([counter+n,val])
            
            if queue:
                if queue[0][0] == counter:
                    heapq.heappush(maxheap,-queue.popleft()[1])

            counter+=1

        return counter

    

        

        