class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #  Check if concatenation condition is met
        if str1 + str2 != str2 + str1:
            return ""
        
        #  Find the GCD of the lengths of str1 and str2
        gcd_length = math.gcd(len(str1), len(str2))
        
        # Return the substring of str1 with length equal to gcd_length
        return str1[:gcd_length]
