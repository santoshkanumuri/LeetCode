# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')
        self.maxpath(root)
        return self.maxi

    

    def maxpath(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        print("here")
        left: int = max(0, self.maxpath(root.left))
        right: int = max(0, self.maxpath(root.right))
        print(left,right)
        self.maxi = max(self.maxi,left + right + root.val)
        
        return (max(left,right) + root.val)
