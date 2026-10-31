class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}

        for coin in coins:
            cache[coin] = 1

        
        def helper(amount):

            if amount == 0:
                return 0
            
            if amount < 0:
                return float("inf")

            if amount in cache:
                return cache[amount]
            
            min_amount = float("inf")

            for coin in coins:
                min_amount = min(min_amount, 1 + helper(amount - coin))

            cache[amount] = min_amount
            return min_amount
        
        ans = helper(amount)
        if ans ==  float("inf"):
            return -1

        else:
            return ans
        
            




        