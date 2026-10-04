class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        res = []
        cur = intervals[0]
        for itr in range(1,len(intervals)):
            if intervals[itr][0] > cur[1]:
                res.append(cur)
                cur = intervals[itr]
                continue
            cur[0] = min(cur[0], intervals[itr][0])
            cur[1] = max(cur[1], intervals[itr][1])
        res.append(cur)
        return res
        