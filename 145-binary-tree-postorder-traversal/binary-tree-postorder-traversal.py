# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def post(self,root,arr):
        if not root:
            return
        self.post(root.left,arr)
        self.post(root.right,arr)
        arr.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        self.post(root,arr)
        return arr

        