# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1=[]
        arr2=[]

        def inorder(root,arr):
            if not root:
                arr.append(root)
                return
            
            arr.append(root.val)
            inorder(root.left,arr)
            inorder(root.right,arr)

        inorder(p,arr1)
        inorder(q,arr2)
        return arr1==arr2
        