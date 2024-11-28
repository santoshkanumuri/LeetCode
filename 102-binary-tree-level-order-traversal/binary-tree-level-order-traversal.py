# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            l = len(q)
            arr=[]
            for i in range(l):
                ele=q.popleft()
                if ele:
                    q.append(ele.left)
                    q.append(ele.right)
                    arr.append(ele.val)
            if arr:
                res.append(arr)
        return res