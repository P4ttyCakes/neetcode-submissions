class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0] * cols for i in range(rows)]

        dp[0][0] = grid[0][0]

        directions = [(-1,0), (0, -1)]

        for row in range(rows):
            for col in range(cols):

                if row == 0 and col == 0:
                    continue

                best = float("inf")

                for dr, dc, in directions:
                    prev_r = row + dr
                    prev_c = col + dc

                    if 0 <= prev_r < rows and 0 <= prev_c < cols:
                        best = min(best, dp[prev_r][prev_c])
                
                dp[row][col] = grid[row][col] + best
        
        return dp[rows - 1][cols - 1]

                



        