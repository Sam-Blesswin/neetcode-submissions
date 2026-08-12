# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map={}
        for i,n in enumerate(inorder):
            map[n]=i

        self.i = 0
        def construct(l,r: int)-> Optional[TreeNode]:
            if l>r:
                return None
            node = TreeNode(preorder[self.i])
            itr = map[preorder[self.i]]
            self.i+=1
            node.left = construct(l, itr-1)
            node.right = construct(itr+1, r)
            return node
            
        return construct(0,len(preorder)-1)
        