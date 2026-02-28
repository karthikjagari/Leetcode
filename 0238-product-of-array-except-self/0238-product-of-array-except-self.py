from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # This will hold our final result

        # Step 1: Compute prefix products
        # prefix holds the product of all elements to the left of index i
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]  # Update prefix for next index

        # Step 2: Compute suffix products and multiply
        # suffix holds the product of all elements to the right of index i
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix  # Multiply by right-side product
            suffix *= nums[i]    # Update suffix for next index

        return answer