class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_index = {int(d): i for i, d in enumerate(digits)}

        for i, d in enumerate(digits):
            current = int(d)
            for bigger in range(9, current, -1):
                if bigger in last_index and last_index[bigger] > i:
                    digits[i], digits[last_index[bigger]] = digits[last_index[bigger]], digits[i]
                    return int("".join(digits))
        return num