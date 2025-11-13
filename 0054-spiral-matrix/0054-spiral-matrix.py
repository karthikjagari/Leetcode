class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        # Define the boundaries
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # Loop until all elements are traversed
        while left <= right and top <= bottom:

            # Step 1: Traverse from left → right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1  # Move top boundary down

            # Step 2: Traverse from top → bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # Move right boundary left

            # Step 3: Traverse from right → left (if rows remain)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1  # Move bottom boundary up

            # Step 4: Traverse from bottom → top (if columns remain)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1  # Move left boundary right

        return res
