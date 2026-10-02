class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(steps, arr):

            if steps == len(nums):
                res.append(arr.copy())
                return
            
            dfs(steps + 1, arr)

            arr.append(nums[steps])
            dfs(steps + 1, arr)

            arr.pop()
        
        dfs(0,[])


        return res

        
        