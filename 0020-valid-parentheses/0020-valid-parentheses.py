class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}  # Matching pairs

        for ch in s:
            if ch in mapping:  # It's a closing bracket
                top_element = stack.pop() if stack else '#'
                if mapping[ch] != top_element:
                    return False
            else:  # It's an opening bracket
                stack.append(ch)
        
        return not stack  # True if stack is empty (all matched)
