class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff=0
        min_price=prices[0]
        for price in prices:
            if(price<min_price):
                min_price=price

            if max_diff < price-min_price:
                max_diff=price-min_price
            

        return max_diff