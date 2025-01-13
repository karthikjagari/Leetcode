class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0  # Left pointer of the sliding window
        max_len = 0  # To store the maximum length of the valid window
        zero_count = 0  # To count the number of zeros in the window

        # array using the right pointer
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1  # Increase z
            # If zero_count exceeds k, shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1  # Decrease zero_count if we are moving past a zero
                left += 1  # Move the left pointer to shrink the window

            # Update the max_len with the current window size
            max_len = max(max_len, right - left + 1)

        return max_len
