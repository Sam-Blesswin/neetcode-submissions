# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt=k
        res = root.val
        def dfs(root: Optional[TreeNode]):
            nonlocal cnt,res
            if not root:
                return
            dfs(root.left)
            if cnt == 0:
                return
            res = root.val
            cnt -= 1
            dfs(root.right)

        dfs(root)
        return res

        