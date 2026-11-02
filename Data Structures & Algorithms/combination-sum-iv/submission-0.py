class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #brute force decision tree
        #and then pick it, however, you could also just add to the set while keeping its position? 

        #you can memo it? somehow? 



        cache = {}

        def helper(nums, target):

            if target == 0:
                return 1
            
            if target < 0:
                return 0
            
            if target in cache:
                return cache[target]

            ans = 0
            for trying in nums:
                ans+=helper(nums, target - trying)
            
            cache[target] = ans
            return ans
        
        return helper(nums, target)
                


            

        
            


            




        
        
        