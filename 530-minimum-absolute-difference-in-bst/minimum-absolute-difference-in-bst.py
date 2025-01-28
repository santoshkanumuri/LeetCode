# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr=[]
        res=float('inf')
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(1,len(arr)):
            res=min(res,arr[i]-arr[i-1])
        print(res)
        return res


