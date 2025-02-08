# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr=[]
        self.pos=0
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.arr.append(root.val)
            inorder(root.right)
        inorder(root)
        return None
        
    def hasNext(self) -> bool:
        return self.pos<len(self.arr)
        
    def next(self) -> int:
        ans=self.arr[self.pos]
        self.pos+=1
        return ans
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()