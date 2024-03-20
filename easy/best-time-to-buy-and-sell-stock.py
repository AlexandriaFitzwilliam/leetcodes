# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # set two markers
        # one tracks from the left
        sell = len(prices) - 1
        # set equal to len of list
        # one from the right
        buy = 0
        # init variable to keep track of current max profit init 0
        max_profit = 0

        for buy, price in enumerate(prices):
            if buy == len(prices) - 1:
                return max_profit
            while buy < sell:
                if prices[sell] - prices[buy] > max_profit:
                    max_profit = prices[sell] - prices[buy]
                sell -= 1
            sell = sell = len(prices) - 1

        # # loop through list
        # # check that left marker is higher index than right
        # #     if not return max profit
        #     while buy < sell:
        #     # subtrack left marker from right marker
        #         if prices[sell] - prices[buy] > max_profit:
        #     # check if current profit is higher than max profit
        #     # if so set max profit
        #             max_profit = prices[sell] - prices[buy]
        #     # -1 from left
        #         buy += 1
        #         sell -= 1

        return max_profit

