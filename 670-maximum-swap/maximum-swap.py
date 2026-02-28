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




"""
        3 LPA Explanation (simple)

Convert number to a list of digits.

Record the last index of each digit.

For each digit, check if a bigger digit exists later.

Swap the first such occurrence and return.

If no swap possible, return original number.

Focus: “I implemented a solution that finds a bigger digit and swaps.”

13 LPA Explanation (detailed, optimal)

Convert the number to a list of digits to access each place easily.

Build a map of last occurrences of each digit.

Traverse digits from left to right because leftmost digits impact the number more.

For each digit, check from 9 down to current+1 if a bigger digit exists later.

Swap with the rightmost bigger digit to maximize the number in one move only.

Return the modified number immediately after swap because only one swap is needed for optimal result.

If no swap is possible, the number is already maximal, so return it.

Focus: “I used a greedy approach, swapping the first digit with the largest possible later digit to maximize the number in a single operation.”   """