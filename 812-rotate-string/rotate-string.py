class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s1=Counter(s)
        s2=Counter(goal)
        if not s1==s2:
            return False
        for i in range(len(s)):
            new=s[i:]+s[:i]
            if new==goal:
                return True
        return False

        