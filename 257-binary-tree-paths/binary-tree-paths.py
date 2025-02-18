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
        
        paths=[]

        def is_leaf(root):
            if not (root.left or root.right):
                return True
        
        def traverse(root,path):
            if not root:
                return False
            path.append(str(root.val))
            if is_leaf(root):
                k=path.copy()
                paths.append(k)
                
            if traverse(root.left, path):
                return True
            if traverse(root.right, path):
                return True
            path.pop()
            return False
        
        traverse(root,[])
        res=[]
        paths=["->".join(path) for path in paths]
        return paths


        