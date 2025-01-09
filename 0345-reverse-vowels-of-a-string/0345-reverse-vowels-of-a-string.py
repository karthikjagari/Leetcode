class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"  # Define vowels
        
        # Convert the string into a list to mutate it
        s = list(s)
        
        # Create an empty list to store vowels from the string
        vowel_list = []
        
        # Loop through the string to collect all vowels
        for char in s:
            if char in vowels:
                vowel_list.append(char)
        
        # Index to track where to place vowels from the list in the string
        vowel_index = len(vowel_list) - 1
        
        # Replace vowels in the original string using the vowel_list
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowel_list[vowel_index]  # Replace with the last vowel in the list
                vowel_index -= 1  # Move to the next vowel from the list
        
        # Join the list back into a string and return it
        return ''.join(s)
