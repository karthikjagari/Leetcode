class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initially set to a very high value
        max_profit = 0            # Initially no profit

        for price in prices:
            # Update the minimum price so far
            if price < min_price:
                min_price = price
            # Calculate potential profit
            profit = price - min_price
            # Update maximum profit if we found a better one
            if profit > max_profit:
                max_profit = profit

        return max_profit
