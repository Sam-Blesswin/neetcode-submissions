# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p,q = q,p

        def dfs(node: TreeNode) -> TreeNode:
            if not node:
                return None
            if p.val <= node.val <= q.val:
                return node
            if q.val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        
        return dfs(root)
        