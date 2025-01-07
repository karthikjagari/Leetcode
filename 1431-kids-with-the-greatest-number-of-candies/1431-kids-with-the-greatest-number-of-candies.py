class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Find the maximum candies manually
        max_candies = candies[0]  # first kid has the most candies
        for candy in candies:
            if candy > max_candies:
                max_candies = candy
        
        
        result = []
        for candy in candies:
            # Add extra candies to the current kid
            total_candies = candy + extraCandies
            # Compare total candies with max_candies
            if total_candies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result
