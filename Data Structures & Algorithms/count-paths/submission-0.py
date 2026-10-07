class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n for i in range(m)]

        dp[0][0] = 1


        for row in range(m):
            for col in range(n):

                for dr, dc in [(-1,0), (0,-1)]:
                    r = row + dr
                    c = col + dc

                    if 0 <= r < m and 0 <= c < n:
                        dp[row][col]+= dp[r][c]
        
        return dp[m-1][n-1]

                    









        