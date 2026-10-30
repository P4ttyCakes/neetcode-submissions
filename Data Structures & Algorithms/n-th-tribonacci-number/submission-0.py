class Solution:
    def tribonacci(self, n: int) -> int:

        cache = {
            0 : 0,
            1 : 1,
            2 : 1
        }
        
        def helper(n):

            if n in cache:
                return cache[n]
            

            res = (helper(n - 1) + helper(n - 2) + helper(n -3))
            cache[n] = res
            return res

        return helper(n) 

        