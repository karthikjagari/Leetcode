class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = []

        n2 = nums2[:]

        for i in nums1:
            if i in n2:
                results.append(i)
                n2.remove(i)
        return results
