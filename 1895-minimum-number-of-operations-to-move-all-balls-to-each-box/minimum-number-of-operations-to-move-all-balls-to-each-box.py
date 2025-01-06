class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(boxes)
        boxes=[int(box) for box in boxes]
        l:int = len(boxes)
        
        res=[0]*l

        for i in range(l):
            for j in range(l):
                res[i]+=abs(j-i) if boxes[j] else 0
                
        
        return res
        