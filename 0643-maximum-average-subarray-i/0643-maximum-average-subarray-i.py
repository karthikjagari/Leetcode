class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        #  sum of the first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum  # Initialize max_sum with the first window sum

        #  Slide the window across the array
        for i in range(k, len(nums)):
            # Update the window sum by adding the next element and removing the first element of the previous window
            window_sum = window_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)  # Update max_sum if current window_sum is larger
        
        # Step 3: Return the maximum average
        return max_sum / k  # Divide the maximum sum by 'k' to get the average