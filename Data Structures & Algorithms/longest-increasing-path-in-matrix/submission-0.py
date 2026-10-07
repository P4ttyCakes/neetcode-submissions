class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows  = len(matrix)
        cols = len(matrix[0])

        dp = [[-1] * cols for i in range(rows)]

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(row, col):

            if dp[row][col] != -1: #if its in the cache, then return it, we've calculated it already
                return dp[row][col]

            best_dir = 0

            for dr, dc in directions: 
                r = row + dr
                c = col + dc
                #if its in bounds
                if 0 <= r < rows and 0 <= c < cols:
                    if matrix[row][col] > matrix[r][c]:
                        best_dir = max(best_dir, dfs(r,c))
                
            dp[row][col] = 1 + best_dir
            return dp[row][col]

                
            


        longest = 0
        
        for row in range(rows):
            for col in range(cols):

                longest = max(longest, dfs(row,col))
        
        return longest 




            