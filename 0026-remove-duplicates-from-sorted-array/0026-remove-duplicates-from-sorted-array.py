class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Pointer for the position to insert the next unique element
        j = 1
        
        # Traverse the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]  # Update the value at position j
                j += 1
        
        return j  # j will be the count of unique elements
