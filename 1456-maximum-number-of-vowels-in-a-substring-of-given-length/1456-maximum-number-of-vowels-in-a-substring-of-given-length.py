class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')  # Store vowels in a set for quick lookup
        current_vowels = 0  #  Start with no vowels in the window
        max_vowels = 0  # Keep track of the maximum vowels found

        # Count vowels in the first window of size `k`
        for i in range(k):
            if s[i] in vowels:  # If the character is a vowel
                current_vowels += 1
        max_vowels = current_vowels  # This is our starting maximum
        
        
        # Slide the window across the string
        for i in range(k, len(s)):
            # Remove the character that's leaving the window
            if s[i - k] in vowels:  # If the outgoing character is a vowel
                current_vowels -= 1
            
            # Add the character that's entering the window
            if s[i] in vowels:  # If the incoming character is a vowel
                current_vowels += 1
            
            # Update the maximum vowels found so far
            max_vowels = max(max_vowels, current_vowels)
            
            

        return max_vowels
