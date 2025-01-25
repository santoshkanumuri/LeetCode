# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        
        def inorder (root,arr):
            if not root:
                return

            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
        
        arr=[]
        inorder(root,arr)
        l=0 
        val=k
        r=len(arr)-1
        while r>0 and l<r:
            key=val-arr[l]
            if key==arr[r]:
                return True
            elif key>arr[r]:
                l+=1
            elif key<arr[r]:
                r-=1
        return False
            

            
        
        