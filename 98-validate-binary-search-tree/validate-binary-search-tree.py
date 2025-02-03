# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBalanced(root,left,right):
            if not root:
                return True
            if root.val<=left or root.val>=right:
                return False
            left = isBalanced(root.left,left,root.val)
            right = isBalanced(root.right,root.val,right)
            return left and right
        return isBalanced(root, float('-inf'), float('inf'))
