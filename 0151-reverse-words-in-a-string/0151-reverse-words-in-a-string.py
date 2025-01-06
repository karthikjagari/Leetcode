class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
    # Reverse the words and join them back with a single space
        return ' '.join(reversed(words))