class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map=defaultdict(int)
        for n in nums:
            map[n] += 1
        bucket = [[] for i in range(len(nums) + 1)]
        for key,val in map.items():
            bucket[val].append(key)
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for n in bucket[i]:
                if k == 0:
                    return res
                res.append(n)
                k-=1
        return res


        