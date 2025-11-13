class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, current_combination):
            # Base case: if the current combination length == digits length
            if index == len(digits):
                result.append(current_combination)
                return

            # Get the letters for the current digit
            letters = phone_map[digits[index]]

            # Try each letter and move to next digit
            for letter in letters:
                backtrack(index + 1, current_combination + letter)

        # Start backtracking from first digit
        backtrack(0, "")
        return result
