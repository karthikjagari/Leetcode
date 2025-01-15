class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #sets are not allowing duplicate thats why we are using sets
        set1 = set(nums1) # gives nums1 without duplicates
        set2 = set(nums2) # gives nums2 without duplicates
        
        only_nums1 = set1 - set2  
        only_nums2 = set2 - set1

        ans = [list(only_nums1), list(only_nums2)]

        return ans