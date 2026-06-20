class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Brute Force Method
        # max_value = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > max_value:
        #             max_value = prices[j] - prices[i]
        # return max_value
        
        l, r = 0, 1
        max_value = 0
        for r in range(len(prices)):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_value = max(profit, max_value)
            else:
                l = r
            r += 1
        return max_value