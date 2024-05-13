from typing import List

class Solution:
    def dot_product(self, matrix1: List[int], matrix2: List[int]) -> int:
        return sum(a * b for a, b in zip(matrix1, matrix2))

    def get_col(self, matrix: List[List[int]], column: int) -> List[int]:
        return [matrix[i][column] for i in range(len(matrix))]

    def inv_col(self, matrix: List[List[int]], column: int) -> None:
        for i in range(len(matrix)):
            matrix[i][column] = 1 - matrix[i][column]

    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ma = [2**(n-j-1) for j in range(n)]  # Corrected power calculation for each column

        # Optimize each row's first element to be 1
        for i in range(m):
            if grid[i][0] == 0:  # Only flip if the most significant bit is 0
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]

        # Optimize columns to have as many 1s as possible
        for j in range(n):
            col = self.get_col(grid, j)
            if sum(col) < m / 2:  # More 0s than 1s, flip the column
                self.inv_col(grid, j)

        # Calculate the final score
        return sum(self.dot_product(row, ma) for row in grid)

# Example usage
sol = Solution()
grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
print(sol.matrixScore(grid))  # Expected output should reflect the maximum score after flips

