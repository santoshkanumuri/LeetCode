class Solution:
    def intToRoman(self, num: int) -> str:
        out=""
        mp={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        chars=list(mp.keys())[::-1]
        nums=list(mp.values())[::-1]
        for i in range(13):
            res=num//nums[i]
            out=out+res*chars[i]
            num=num%nums[i]
        return out
       

        