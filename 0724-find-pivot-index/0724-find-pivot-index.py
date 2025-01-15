class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        index = 0
        

        for num in nums:
            right_sum = total - left_sum -num # gives right sum
            if left_sum == right_sum:
                return index #if both are equal return current index
            left_sum += num # else increase the left_sum with index
            index += 1
        return -1