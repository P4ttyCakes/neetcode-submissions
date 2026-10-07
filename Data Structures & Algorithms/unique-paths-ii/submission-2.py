class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0] * cols for i in range(rows)]

        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0
        
        else:
            dp[0][0] = 1
            

        for row in range(rows):
            for col in range(cols):

                #if current cell is an obstacle:

                if obstacleGrid[row][col] == 1:
                    continue

                for dr, dc in [(0,-1), (-1,0)]:
                    prev_r = row + dr
                    prev_c = col + dc

                    if 0 <= prev_r < rows and 0 <= prev_c < cols:
                        dp[row][col] += dp[prev_r][prev_c]
        
        return dp[rows -1][cols - 1]







        