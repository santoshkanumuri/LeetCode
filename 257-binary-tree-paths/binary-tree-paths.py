# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        paths = []

        def traverse(root,path):
            if not root:
                return 
            path = path + str(root.val)
            if not (root.left or root.right):
                paths.append(path)
                
            if root.left:
                traverse(root.left, path + "->")
                
            if root.right:
                traverse(root.right, path + "->")

            return 
        
        traverse(root, "")
        
        return paths


        