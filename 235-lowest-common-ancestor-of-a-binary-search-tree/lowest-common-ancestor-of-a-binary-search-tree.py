# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        p=p.val
        q=q.val
        while root:
            if root.val>p and root.val>q:
                root=root.left
            elif root.val<p and root.val<q:
                root=root.right
            else:
                return root

            
                