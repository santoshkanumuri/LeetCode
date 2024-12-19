# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.res=None
        def inorder(ori,cl):
            if not ori:
                return 
            inorder(ori.left,cl.left)
            if ori==self.target:
                self.res=cl
            inorder(ori.right,cl.right)

        self.target=target
        inorder(original,cloned)
        return self.res
