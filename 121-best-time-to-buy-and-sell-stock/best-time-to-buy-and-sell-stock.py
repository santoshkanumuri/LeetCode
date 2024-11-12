class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n:int=len(prices)
        mn=1000000
        profit=0
        for i in range(n):
            p=prices[i]
            mn=min(mn,p)
            profit=max(profit,p-mn)
        return profit

        