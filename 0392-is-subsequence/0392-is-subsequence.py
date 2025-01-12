class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Two pointers for s and t
        # Traverse `t` while comparing with `s`
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # Check if characters match
                i += 1  # Move pointer `i` (traverse `s`)
            j += 1  # Move pointer `j` (traverse `t`)
        
        return i == len(s)
        
        