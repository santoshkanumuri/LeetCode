class Solution:
    def intToRoman(self, num: int) -> str:
        out=""
        mp={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        chars=list(mp.keys())[::-1]
        nums=list(mp.values())[::-1]
        while num>=1:
            print(num,out)
            for i in range(13):
                n=nums[i]
                if num>=n:
                    num=num-n
                    out=out+chars[i]
                    break
        return out
       

        