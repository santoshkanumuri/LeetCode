class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if not Counter(s)==Counter(goal):
            return False

        new=s+s
        return goal in new

        