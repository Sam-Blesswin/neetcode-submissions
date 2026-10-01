class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(itr:int, arr:List[int]):
            if itr == len(nums):
                res.append(arr.copy())
                return

            arr.append(nums[itr])
            dfs(itr+1,arr)
            while itr<len(nums) and nums[itr] == arr[-1]:
                itr+=1
            arr.remove(arr[-1])
            dfs(itr,arr)
            

        dfs(0,[])
        return res
        