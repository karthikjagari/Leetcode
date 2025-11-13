# 242. Valid Anagram
# Author: Karthik Jagari

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are not equal, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Use Counter to count frequency of each character
        return Counter(s) == Counter(t)
