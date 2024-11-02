class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        li=list(sentence.strip().split())
        if not sentence[-1]==sentence[0]:
            return False
        for i in range(len(li)-1):
            print(li[i])
            if li[i][-1]!=li[i+1][0]:
                return False
        return True
        