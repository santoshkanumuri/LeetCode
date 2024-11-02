class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if not sentence[-1]==sentence[0]:
            return False
        for i in range(len(sentence)):
            char=sentence[i]
            if char==" ":
                if sentence[i-1]!=sentence[i+1]:
                    return False
        return True
        