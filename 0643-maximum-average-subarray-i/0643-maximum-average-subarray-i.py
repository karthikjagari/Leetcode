class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # sum of the first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            # Slide the window: add the next element and subtract the element that is leaving the window
            temp = nums[i] - nums[i - k]
            current_sum += temp
            # Update max_sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
      
        return max_sum / k
