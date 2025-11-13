class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_index = {int(d): i for i, d in enumerate(digits)}  # record last index of each digit

        # Traverse each digit
        for i, d in enumerate(digits):
            current = int(d)
            # Check if there's a bigger digit available later
            for bigger in range(9, current, -1):
                if bigger in last_index and last_index[bigger] > i:
                    # Swap current with that bigger digit
                    digits[i], digits[last_index[bigger]] = digits[last_index[bigger]], digits[i]
                    return int("".join(digits))

        # If no swap made, return original number
        return num
