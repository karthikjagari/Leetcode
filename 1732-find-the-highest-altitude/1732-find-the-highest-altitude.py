class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0 
        current = 0 
        for g in gain:
            current += g
            high = max(high , current)
        return high