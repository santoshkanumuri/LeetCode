class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for i in range(12):
            for j in range(60):
                var = bin(i)+bin(j)
                if str(var).count("1") == turnedOn:
                    s = str(i)+":"+str(j) if j>9 else str(i)+":"+"0"+str(j)
                    res.append(s)
        return res

        