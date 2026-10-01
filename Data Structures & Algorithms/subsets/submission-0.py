class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(itr:int, arr:List[int]):
            if itr == len(nums):
                res.append(arr.copy())
                return

            dfs(itr+1, arr)
            arr.append(nums[itr])
            dfs(itr+1,arr)
            arr.remove(arr[-1])
        dfs(0,[])
        return res


        