class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # num = set(nums1)
        # nums = set(nums2)
         
        return list(set(nums1) & set(nums2))