class Solution:
    def intToRoman(self, num: int) -> str:
        out=""
        nums=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        chars=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        for i in range(13):
            res=num//nums[i]
            out=out+res*chars[i]
            num=num%nums[i]
        return out
       

        