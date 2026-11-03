import math

class Solution:
    def numSquares(self, n: int) -> int:

        def is_perfect_square(n):
            if n < 0:
                return False
            root = math.isqrt(n)
            return root * root == n

        perfect_squares = []
        for i in range(1, n + 1):
            if is_perfect_square(i):
                perfect_squares.append(i)

        

        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in perfect_squares:
                if square > i:
                    break
                
                dp[i] = min(1 + dp[i - square], dp[i]) 
        
        return dp[n]





    


            