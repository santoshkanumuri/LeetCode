class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(boxes)
        boxes=[int(box) for box in boxes]
        l:int = len(boxes)
        
        left=[0]*l
        right=[0]*l

        balls=0
        moves=0
        for i in range(l):
            left[i]=balls+moves
            balls+=1 if boxes[i] else 0
            moves=left[i]
        balls=0
        moves=0
        for i in reversed(range(l)):
            right[i]=balls+moves
            balls+=1 if boxes[i] else 0
            moves=right[i]
            right[i]+=left[i]
        
        return right
        
        
        


        
        