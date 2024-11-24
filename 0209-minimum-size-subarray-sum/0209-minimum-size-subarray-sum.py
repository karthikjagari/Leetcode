class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
       
        l = 0
        curr_sum = 0
        min_len = float('inf')
        
       
        for r in range(len(nums)):
            curr_sum += nums[r] 
            
            while curr_sum >= target:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]  # Remove the element at the left pointer
                l += 1  # Shrink the window from the left
        
        # If min_length was updated, return it; otherwise, return 0
        return min_len if min_len != float('inf') else 0
