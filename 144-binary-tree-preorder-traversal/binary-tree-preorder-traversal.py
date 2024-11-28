# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pre(self,root,arr):
        if not root:
            return 

        arr.append(root.val)
        self.pre(root.left,arr)
        self.pre(root.right,arr)

        
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        self.pre(root,arr)
        return arr
        
        