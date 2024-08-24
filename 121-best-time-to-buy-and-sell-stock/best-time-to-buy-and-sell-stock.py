class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff=0
        min_num=prices[0]
        for num in prices:
            min_num=min(num,min_num)
            max_diff=max(max_diff,num-min_num)
            print(max_diff)
        return max_diff