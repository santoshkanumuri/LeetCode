# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def pt(node):
            if not node:
                return None
            
            if node==p or node==q:
                print(node.val)
                return node

            left=pt(node.left)
            right=pt(node.right)

            if left and right:
                return node

            return left or right
        return pt(root)
        
        