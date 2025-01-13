class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0  # To store the maximum number of consecutive 1's
        current_count = 0  # To store the current streak of consecutive 1's

        # Iterate through the list
        for num in nums:
            if num == 1:
                current_count += 1  # Increase the streak of 1's
            else:
                current_count = 0  # Reset streak when encountering a 0

            # Update the maximum streak
            max_count = max(max_count, current_count)

        return max_count
