class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        index = 0


        for num in nums:
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return index

            left_sum += num
            index +=1
        return -1