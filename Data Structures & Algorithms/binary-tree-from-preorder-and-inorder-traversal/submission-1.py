# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap ={}
        for i,n in enumerate(inorder):
            hashmap[n]=i

        self.itr = 0
        def dfs(i,j):
            if i>=j:
                return None

            node = TreeNode(preorder[self.itr])
            pos = hashmap[preorder[self.itr]]
            self.itr+=1

            node.left = dfs(i, pos)
            node.right = dfs(pos+1, j)

            return node
            

        return dfs(0,len(preorder))

        