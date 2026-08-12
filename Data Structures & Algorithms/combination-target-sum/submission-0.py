class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted(nums)
        res = []
        def dfs(itr,sum:int, arr:List[int]):
            if itr >= len(nums) or sum>target:
                return
            if sum == target:
                res.append(arr.copy())
                return
            arr.append(nums[itr])
            dfs(itr,sum+nums[itr],arr)
            arr.pop()
            dfs(itr+1,sum,arr)

        dfs(0,0,[])
        return res
        