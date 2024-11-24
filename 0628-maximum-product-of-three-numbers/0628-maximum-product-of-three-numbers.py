class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
       
        nums.sort()
        
        
        max_1 = nums[-1] * nums[-2] * nums[-3]
        max_2 = nums[0] * nums[1] * nums[-1]
        
        
        return max(max_1, max_2)

        