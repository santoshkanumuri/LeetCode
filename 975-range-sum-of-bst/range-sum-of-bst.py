# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total=0
        def traverse(root,low,high):
            if not root:
                return
            if root.val>=low and root.val<=high:
                self.total=self.total+root.val 
            traverse(root.left,low,high)    
            traverse(root.right,low,high)   
            return self.total

        
        t=traverse(root,low,high)
        return t
        