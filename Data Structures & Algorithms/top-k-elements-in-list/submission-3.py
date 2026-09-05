class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n]+=1
        bucket=[[] for _ in range(N+1)]
        for key,value in hashmap.items():
            bucket[value].append(key)
        res=[]
        for i in range(N,-1,-1):
            for v in bucket[i]:
                if len(res) == k:
                    break
                res.append(v)
        return res


        




        