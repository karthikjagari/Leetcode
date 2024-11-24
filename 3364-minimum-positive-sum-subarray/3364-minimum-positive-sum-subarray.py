class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        found = False
    
        for length in range(l, r + 1):
            # initial window sum
            window_sum = sum(nums[:length])
            
            # initial window has a valid sum
            if window_sum > 0:
                min_sum = min(min_sum, window_sum)
                found = True
            
            # Slide the window across the array
            for i in range(length, n):
                window_sum += nums[i] - nums[i - length]
                
                #  current window sum is valid
                if window_sum > 0:
                    min_sum = min(min_sum, window_sum)
                    found = True
        
        
        return min_sum if found else -1